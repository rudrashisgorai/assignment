from fastapi import FastAPI
import os
import json
import numpy as np 
import pandas as pd 
from rapidfuzz import fuzz, process
with open("DatasetMapping.json", "r" , encoding = "utf8") as f:
    data_json = json.load(f)

data_df = pd.DataFrame(data_json)
data_df['brand_name']= data_df['brand_name'].str.strip()
data_df['company_name']= data_df['company_name'].str.strip()
company_name_map ={ i: [] for i in data_df['company_name'].value_counts().keys()}
company_name_list  =list(company_name_map.keys())
for a,b in (zip(data_df.index , data_df['company_name'])):
    company_name_map[b].append(a)

def clean_text(user_input):
    try:
        return user_input.strip().upper()
    except Exception as e:
        pass

def check(brand_input ,db):
    try:
        brand_input = clean_text(brand_input)
        # op = process.extract(company_input,db.company_name.,scorer=fuzz.WRatio,limit=10)
        brand_matches = process.extract(brand_input,db.brand_name,scorer=fuzz.WRatio,limit=10)
        brand_match = brand_matches[0]
        return {'row' : brand_match[2], 'conf_level' :brand_match[1]}
    except Exception as e:
        print(e)

def get_row_json(brand_input , df, company_matches_map):
    try:
        check_get_val = check(brand_input , df)
        output_dict= df.loc[check_get_val['row']].to_dict()
        check_get_val['conf_level'] = check_get_val['conf_level']* company_matches_map[output_dict['company_name']]/100
        return {**output_dict, **check_get_val}
    except Exception as e:
            print(e) 
    
def final_match(brand_input, company_input,company_name_map,company_name_list, data_df):
        try:
            company_input = clean_text(company_input)
            THRESHOLD_COMPANY_MATCH = int(os.getenv('THRESHOLD_COMPANY_MATCH'))
            company_matches = process.extract(company_input,company_name_list,scorer=fuzz.WRatio,limit= THRESHOLD_COMPANY_MATCH) # top 3 company matches companies retireved
            company_matches_map = {i[0]: i[1] for i in company_matches} #map of company name and conf_level of the match
            df_case =pd.DataFrame(columns=data_df.columns) #narrowed down list of brand_inputs
            for i in company_matches:
                df_case = pd.concat([df_case, data_df.iloc[company_name_map[i[0]]]])
            return {'code' : 200 ,**get_row_json(brand_input, df_case,company_matches_map)}
        except Exception as e:
            print(e) 
            return {'code' : 401}

#api code begins

app = FastAPI()


@app.get('/')
async def assignment(brand: str , company: str):
    
    try: 
        match = final_match(brand, company,company_name_map,company_name_list, data_df)
        THRESHOLD_CONF_LEVEL = int(os.getenv('THRESHOLD_CONF_LEVEL'))
        if match['conf_level'] < THRESHOLD_CONF_LEVEL:
            return {'code' :404}
        else :
             return match
    except Exception as e:
        print(e)
        return {
        'code' : 400
        }
        
    
    