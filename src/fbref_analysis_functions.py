### Import necessary packages

import requests
import pandas as pd
from bs4 import BeautifulSoup
import klib as kb
import seaborn as sb
import matplotlib.pyplot as plt
import wes
import matplotlib as mpl
import warnings
import numpy as np
from math import pi

warnings.filterwarnings("ignore")

def Convert(string):
    li = list(string.split(" "))
    return li

### Get player data

def get_player_data(x):
    warnings.filterwarnings("ignore")
    url = x
    page =requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = [element.text for element in soup.find_all("span")]
    name = name[7]
    metric_names = []
    metric_values = []
    remove_content = ["'", "[", "]", ","]
    for row in soup.findAll('table')[0].tbody.findAll('tr'):
        first_column = row.findAll('th')[0].contents
        metric_names.append(first_column)
    for row in soup.findAll('table')[0].tbody.findAll('tr'):
        first_column = row.findAll('td')[0].contents
        metric_values.append(first_column)
    metric_values = repr(metric_values)
    for content in remove_content:
        metric_values = metric_values.replace(content, '')
    metric_values = Convert(metric_values)
    df_player = pd.DataFrame()
    df_player['Name'] = name[0]
    df_player[metric_names[0]] = []
    df_player[metric_names[1]] = []
    df_player[metric_names[2]] = []
    df_player[metric_names[3]] = []
    df_player[metric_names[4]] = []
    df_player[metric_names[5]] = []
    df_player[metric_names[6]] = []
    df_player[metric_names[8]] = []
    df_player[metric_names[9]] = []
    df_player[metric_names[10]] = []
    df_player[metric_names[11]] = []
    df_player[metric_names[12]] = []
    df_player[metric_names[13]] = []
    df_player[metric_names[14]] = []
    df_player[metric_names[16]] = []
    df_player[metric_names[17]] = []
    df_player[metric_names[18]] = []
    df_player[metric_names[19]] = []
    df_player[metric_names[20]] = []
    df_player[metric_names[21]] = []
    df_player = kb.clean_column_names(df_player)
    name = name
    non_penalty_goals = (metric_values[0])
    npx_g = metric_values[1]
    shots_total = metric_values[2]
    assists = metric_values[3]
    x_a = metric_values[4]
    npx_g_plus_x_a = metric_values[5] 
    shot_creating_actions = metric_values[6] 
    passes_attempted = metric_values[8] 
    pass_completion_percent = metric_values[9] 
    progressive_passes = metric_values[10] 
    progressive_carries = metric_values[11] 
    dribbles_completed = metric_values[12] 
    touches_att_pen = metric_values[13]
    progressive_passes_rec = metric_values[14] 
    pressures = metric_values[16] 
    tackles = metric_values[17] 
    interceptions = metric_values[18] 
    blocks = metric_values[19]
    clearances = metric_values[20]
    aerials_won = metric_values[21]
    df_player.loc[0] = [name, non_penalty_goals, npx_g, shots_total, assists, x_a, npx_g_plus_x_a, shot_creating_actions, passes_attempted, pass_completion_percent,
                       progressive_passes, progressive_carries, dribbles_completed, touches_att_pen, progressive_passes_rec, pressures, tackles, interceptions, blocks,
                       clearances, aerials_won] 
    return df_player


    
### Compare two players

def compare_players_data(x, y):
    
    warnings.filterwarnings("ignore")
    
    url_x = x
    url_y = y
    
    page_x =requests.get(url_x)
    page_y =requests.get(url_y)
    
    soup_x = BeautifulSoup(page_x.content, 'html.parser')
    soup_y = BeautifulSoup(page_y.content, 'html.parser')
    
    name_x = [element.text for element in soup_x.find_all("span")]
    name_y = [element.text for element in soup_y.find_all("span")]
    
    name_x = name_x[7]
    name_y = name_y[7]
    
    metric_names_x = []
    metric_names_y = []
    
    metric_values_x = []
    metric_values_y = []
    
    remove_content = ["'", "[", "]", ",", "%"]
    
    for row in soup_x.findAll('table')[0].tbody.findAll('tr'):
        first_column_x = row.findAll('th')[0].contents
        metric_names_x.append(first_column_x)
        
    for row in soup_y.findAll('table')[0].tbody.findAll('tr'):
        first_column_y = row.findAll('th')[0].contents
        metric_names_y.append(first_column_y)
        
    for row in soup_x.findAll('table')[0].tbody.findAll('tr'):
        first_column_x_x = row.findAll('td')[0].contents
        metric_values_x.append(first_column_x_x)
    
    for row in soup_y.findAll('table')[0].tbody.findAll('tr'):
        first_column_y_y = row.findAll('td')[0].contents
        metric_values_y.append(first_column_y_y)
        
    metric_values_x = repr(metric_values_x) 
    
    metric_values_y = repr(metric_values_y)
    
    for content in remove_content:
        metric_values_x = metric_values_x.replace(content, '')
    
    for content in remove_content:
        metric_values_y = metric_values_y.replace(content, '')
    
    metric_values_x = Convert(metric_values_x)
    
    metric_values_y = Convert(metric_values_y)
    
    df_player_1 = pd.DataFrame()
    
    df_player_2 = pd.DataFrame()
    
    df_player_1['Name'] = name_x[0]
    df_player_1[metric_names_x[0]] = []
    df_player_1[metric_names_x[1]] = []
    df_player_1[metric_names_x[2]] = []
    df_player_1[metric_names_x[3]] = []
    df_player_1[metric_names_x[4]] = []
    df_player_1[metric_names_x[5]] = []
    df_player_1[metric_names_x[6]] = []
    df_player_1[metric_names_x[8]] = []
    df_player_1[metric_names_x[9]] = []
    df_player_1[metric_names_x[10]] = []
    df_player_1[metric_names_x[11]] = []
    df_player_1[metric_names_x[12]] = []
    df_player_1[metric_names_x[13]] = []
    df_player_1[metric_names_x[14]] = []
    df_player_1[metric_names_x[16]] = []
    df_player_1[metric_names_x[17]] = []
    df_player_1[metric_names_x[18]] = []
    df_player_1[metric_names_x[19]] = []
    df_player_1[metric_names_x[20]] = []
    df_player_1[metric_names_x[21]] = []
    
    df_player_2['Name'] = name_x[0]
    df_player_2[metric_names_y[0]] = []
    df_player_2[metric_names_y[1]] = []
    df_player_2[metric_names_y[2]] = []
    df_player_2[metric_names_y[3]] = []
    df_player_2[metric_names_y[4]] = []
    df_player_2[metric_names_y[5]] = []
    df_player_2[metric_names_y[6]] = []
    df_player_2[metric_names_y[8]] = []
    df_player_2[metric_names_y[9]] = []
    df_player_2[metric_names_y[10]] = []
    df_player_2[metric_names_y[11]] = []
    df_player_2[metric_names_y[12]] = []
    df_player_2[metric_names_y[13]] = []
    df_player_2[metric_names_y[14]] = []
    df_player_2[metric_names_y[16]] = []
    df_player_2[metric_names_y[17]] = []
    df_player_2[metric_names_y[18]] = []
    df_player_2[metric_names_y[19]] = []
    df_player_2[metric_names_y[20]] = []
    df_player_2[metric_names_y[21]] = []
    
    df_player_1 = kb.clean_column_names(df_player_1)
    df_player_2 = kb.clean_column_names(df_player_2)
    
    name_x = name_x
    non_penalty_goals_x = (metric_values_x[0])
    npx_g_x = metric_values_x[1]
    shots_total_x = metric_values_x[2]
    assists_x = metric_values_x[3]
    x_a_x = metric_values_x[4]
    npx_g_plus_x_a_x = metric_values_x[5] 
    shot_creating_actions_x = metric_values_x[6] 
    passes_attempted_x = metric_values_x[8] 
    pass_completion_percent_x = metric_values_x[9] 
    progressive_passes_x = metric_values_x[10] 
    progressive_carries_x = metric_values_x[11] 
    dribbles_completed_x = metric_values_x[12] 
    touches_att_pen_x = metric_values_x[13]
    progressive_passes_rec_x = metric_values_x[14] 
    pressures_x = metric_values_x[16] 
    tackles_x = metric_values_x[17] 
    interceptions_x = metric_values_x[18] 
    blocks_x = metric_values_x[19]
    clearances_x = metric_values_x[20]
    aerials_won_x = metric_values_x[21]
    
    df_player_1.loc[0] = [name_x, non_penalty_goals_x, npx_g_x, shots_total_x, assists_x, x_a_x, npx_g_plus_x_a_x, shot_creating_actions_x, passes_attempted_x, pass_completion_percent_x,
                       progressive_passes_x, progressive_carries_x, dribbles_completed_x, touches_att_pen_x, progressive_passes_rec_x, pressures_x, tackles_x, interceptions_x, blocks_x,
                       clearances_x, aerials_won_x]
    
    name_y = name_y
    non_penalty_goals_y = (metric_values_y[0])
    npx_g_y = metric_values_y[1]
    shots_total_y = metric_values_y[2]
    assists_y = metric_values_y[3]
    x_a_y = metric_values_y[4]
    npx_g_plus_x_a_y = metric_values_y[5] 
    shot_creating_actions_y = metric_values_y[6] 
    passes_attempted_y = metric_values_y[8] 
    pass_completion_percent_y = metric_values_y[9] 
    progressive_passes_y = metric_values_y[10] 
    progressive_carries_y = metric_values_y[11] 
    dribbles_completed_y = metric_values_y[12] 
    touches_att_pen_y = metric_values_y[13]
    progressive_passes_rec_y = metric_values_y[14] 
    pressures_y = metric_values_y[16] 
    tackles_y = metric_values_y[17] 
    interceptions_y = metric_values_y[18] 
    blocks_y = metric_values_y[19]
    clearances_y = metric_values_y[20]
    aerials_won_y = metric_values_y[21]
    
    df_player_2.loc[0] = [name_y, non_penalty_goals_y, npx_g_y, shots_total_y, assists_y, x_a_y, npx_g_plus_x_a_y, shot_creating_actions_y, passes_attempted_y, pass_completion_percent_y,
                       progressive_passes_y, progressive_carries_y, dribbles_completed_y, touches_att_pen_y, progressive_passes_rec_y, pressures_y, tackles_y, interceptions_y, blocks_y,
                       clearances_y, aerials_won_y]
    
    df_player_comp = pd.concat([df_player_1, df_player_2])
    
    df_player_comp[['non_penalty_goals', 'npx_g', 'shots_total', 'assists', 'x_a', 'npx_g_plus_x_a', 'shot_creating_actions', 'passes_attempted', 'pass_completion_percent',
                       'progressive_passes', 'progressive_carries', 'dribbles_completed', 'touches_att_pen', 'progressive_passes_rec', 'pressures', 'tackles', 'interceptions', 'blocks',
                       'clearances', 'aerials_won']] = df_player_comp[['non_penalty_goals', 'npx_g', 'shots_total', 'assists', 'x_a', 'npx_g_plus_x_a', 'shot_creating_actions', 'passes_attempted', 'pass_completion_percent',
                       'progressive_passes', 'progressive_carries', 'dribbles_completed', 'touches_att_pen', 'progressive_passes_rec', 'pressures', 'tackles', 'interceptions', 'blocks',
                       'clearances', 'aerials_won']].apply(pd.to_numeric)
    
    wes.set_palette("Royal1")
    
    fig, ax =plt.subplots(1,8, figsize=(40,5))
    sb.barplot(df_player_comp['name'], df_player_comp['non_penalty_goals'], ax=ax[0]).set(title='Non Penalty Goals')
    sb.barplot(df_player_comp['name'], df_player_comp['npx_g'], ax=ax[1]).set(title='Non Penalty xG')
    sb.barplot(df_player_comp['name'], df_player_comp['shots_total'], ax=ax[2]).set(title='Total Shots')
    sb.barplot(df_player_comp['name'], df_player_comp['assists'], ax=ax[3]).set(title='Total Assists')
    sb.barplot(df_player_comp['name'], df_player_comp['shot_creating_actions'], ax=ax[4]).set(title='Shot Creating Actions')
    sb.barplot(df_player_comp['name'], df_player_comp['pass_completion_percent'], ax=ax[5]).set(title='Pass Completion %')
    sb.barplot(df_player_comp['name'], df_player_comp['progressive_passes'], ax=ax[6]).set(title='Progressive Passes')
    sb.barplot(df_player_comp['name'], df_player_comp['progressive_carries'], ax=ax[7]).set(title='Progressive Carries')
   
    
    fig, ax =plt.subplots(1,8, figsize=(40,5))
    sb.barplot(df_player_comp['name'], df_player_comp['dribbles_completed'], ax=ax[0]).set(title='Dribbles Completed')
    sb.barplot(df_player_comp['name'], df_player_comp['touches_att_pen'], ax=ax[1]).set(title='Touches in Pen Area')
    sb.barplot(df_player_comp['name'], df_player_comp['aerials_won'], ax=ax[2]).set(title='Aerials Won')
    sb.barplot(df_player_comp['name'], df_player_comp['progressive_passes_rec'], ax=ax[3]).set(title='Progressive Passes Received')
    sb.barplot(df_player_comp['name'], df_player_comp['pressures'], ax=ax[4]).set(title='Pressures')
    sb.barplot(df_player_comp['name'], df_player_comp['tackles'], ax=ax[5]).set(title='Tackles')
    sb.barplot(df_player_comp['name'], df_player_comp['interceptions'], ax=ax[6]).set(title='Interceptions')
    sb.barplot(df_player_comp['name'], df_player_comp['blocks'], ax=ax[7]).set(title='Blocks')
    
    
### Compare percentiles of two players on radar chart
    
def compare_players_percentile(x,y):
    
    warnings.filterwarnings("ignore")
    
    url_x = x
    url_y = y
    
    page_x =requests.get(url_x)
    page_y =requests.get(url_y)
    
    soup_x = BeautifulSoup(page_x.content, 'html.parser')
    soup_y = BeautifulSoup(page_y.content, 'html.parser')
    
    name_x = [element.text for element in soup_x.find_all("span")]
    name_y = [element.text for element in soup_y.find_all("span")]
    
    name_x = name_x[7]
    name_y = name_y[7]
    
    metric_names_x = []
    metric_names_y = []
    
    metric_values_x = []
    metric_values_y = []
    
    remove_content = ["'", "[", "]", ",", "%"]
    
    for row in soup_x.findAll('table')[0].tbody.findAll('tr'):
        first_column_x = row.findAll('th')[0].contents
        metric_names_x.append(first_column_x)
        
    for row in soup_y.findAll('table')[0].tbody.findAll('tr'):
        first_column_y = row.findAll('th')[0].contents
        metric_names_y.append(first_column_y)
        
    for row in soup_x.findAll('table')[0].tbody.findAll('tr'):
        first_column_x = row.findAll('td')[1].contents
        metric_values_x.append(first_column_x)
        
    for row in soup_y.findAll('table')[0].tbody.findAll('tr'):
        first_column_y = row.findAll('td')[1].contents
        metric_values_y.append(first_column_y)
        
    clean_left_x = []
    splitat_r = 65
    splitat_l = 67

    for item in metric_values_x:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_left_x.append(left)

    clean_overall_x = []
    
    for item in clean_left_x:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_overall_x.append(right)
    
    clean_x = []
    
    for item in clean_overall_x:
        item = item.replace("<","")
        clean_x.append(item)
        
    clean_left_y = []
    splitat_r = 65
    splitat_l = 67

    for item in metric_values_y:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_left_y.append(left)

    clean_overall_y = []
    
    for item in clean_left_y:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_overall_y.append(right)
    
    clean_y = []
    
    for item in clean_overall_y:
        item = item.replace("<","")
        clean_y.append(item)
        
    df_player_1 = pd.DataFrame()
    
    df_player_2 = pd.DataFrame()
    
    df_player_1['Name'] = name_x[0]
    df_player_1[metric_names_x[0]] = []
    df_player_1[metric_names_x[1]] = []
    df_player_1[metric_names_x[2]] = []
    df_player_1[metric_names_x[3]] = []
    df_player_1[metric_names_x[4]] = []
    df_player_1[metric_names_x[5]] = []
    df_player_1[metric_names_x[6]] = []
    df_player_1[metric_names_x[8]] = []
    df_player_1[metric_names_x[9]] = []
    df_player_1[metric_names_x[10]] = []
    df_player_1[metric_names_x[11]] = []
    df_player_1[metric_names_x[12]] = []
    df_player_1[metric_names_x[13]] = []
    df_player_1[metric_names_x[14]] = []
    df_player_1[metric_names_x[16]] = []
    df_player_1[metric_names_x[17]] = []
    df_player_1[metric_names_x[18]] = []
    df_player_1[metric_names_x[19]] = []
    df_player_1[metric_names_x[20]] = []
    df_player_1[metric_names_x[21]] = []
    
    df_player_2['Name'] = name_x[0]
    df_player_2[metric_names_y[0]] = []
    df_player_2[metric_names_y[1]] = []
    df_player_2[metric_names_y[2]] = []
    df_player_2[metric_names_y[3]] = []
    df_player_2[metric_names_y[4]] = []
    df_player_2[metric_names_y[5]] = []
    df_player_2[metric_names_y[6]] = []
    df_player_2[metric_names_y[8]] = []
    df_player_2[metric_names_y[9]] = []
    df_player_2[metric_names_y[10]] = []
    df_player_2[metric_names_y[11]] = []
    df_player_2[metric_names_y[12]] = []
    df_player_2[metric_names_y[13]] = []
    df_player_2[metric_names_y[14]] = []
    df_player_2[metric_names_y[16]] = []
    df_player_2[metric_names_y[17]] = []
    df_player_2[metric_names_y[18]] = []
    df_player_2[metric_names_y[19]] = []
    df_player_2[metric_names_y[20]] = []
    df_player_2[metric_names_y[21]] = []
    
    df_player_1 = kb.clean_column_names(df_player_1)
    df_player_2 = kb.clean_column_names(df_player_2)
        
    name_x = name_x
    non_penalty_goals_x = (clean_x[0])
    npx_g_x = clean_x[1]
    shots_total_x = clean_x[2]
    assists_x = clean_x[3]
    x_a_x = clean_x[4]
    npx_g_plus_x_a_x = clean_x[5] 
    shot_creating_actions_x = clean_x[6] 
    passes_attempted_x = clean_x[8] 
    pass_completion_percent_x = clean_x[9] 
    progressive_passes_x = clean_x[10] 
    progressive_carries_x = clean_x[11] 
    dribbles_completed_x = clean_x[12] 
    touches_att_pen_x = clean_x[13]
    progressive_passes_rec_x = clean_x[14] 
    pressures_x = clean_x[16] 
    tackles_x = clean_x[17] 
    interceptions_x = clean_x[18] 
    blocks_x = clean_x[19]
    clearances_x = clean_x[20]
    aerials_won_x = clean_x[21]
    
    df_player_1.loc[0] = [name_x, non_penalty_goals_x, npx_g_x, shots_total_x, assists_x, x_a_x, npx_g_plus_x_a_x, shot_creating_actions_x, passes_attempted_x, pass_completion_percent_x,
                       progressive_passes_x, progressive_carries_x, dribbles_completed_x, touches_att_pen_x, progressive_passes_rec_x, pressures_x, tackles_x, interceptions_x, blocks_x,
                       clearances_x, aerials_won_x]
    
    name_y = name_y
    non_penalty_goals_y = (clean_y[0])
    npx_g_y = clean_y[1]
    shots_total_y = clean_y[2]
    assists_y = clean_y[3]
    x_a_y = clean_y[4]
    npx_g_plus_x_a_y = clean_y[5] 
    shot_creating_actions_y = clean_y[6] 
    passes_attempted_y = clean_y[8] 
    pass_completion_percent_y = clean_y[9] 
    progressive_passes_y = clean_y[10] 
    progressive_carries_y = clean_y[11] 
    dribbles_completed_y = clean_y[12] 
    touches_att_pen_y = clean_y[13]
    progressive_passes_rec_y = clean_y[14] 
    pressures_y = clean_y[16] 
    tackles_y = clean_y[17] 
    interceptions_y = clean_y[18] 
    blocks_y = clean_y[19]
    clearances_y = clean_y[20]
    aerials_won_y = clean_y[21]
    
    df_player_2.loc[0] = [name_y, non_penalty_goals_y, npx_g_y, shots_total_y, assists_y, x_a_y, npx_g_plus_x_a_y, shot_creating_actions_y, passes_attempted_y, pass_completion_percent_y,
                       progressive_passes_y, progressive_carries_y, dribbles_completed_y, touches_att_pen_y, progressive_passes_rec_y, pressures_y, tackles_y, interceptions_y, blocks_y,
                       clearances_y, aerials_won_y]
    
    df_player_comp = pd.concat([df_player_1, df_player_2])
    
    df_player_comp[['non_penalty_goals', 'npx_g', 'shots_total', 'assists', 'x_a', 'npx_g_plus_x_a', 'shot_creating_actions', 'passes_attempted', 'pass_completion_percent',
                       'progressive_passes', 'progressive_carries', 'dribbles_completed', 'touches_att_pen', 'progressive_passes_rec', 'pressures', 'tackles', 'interceptions', 'blocks',
                       'clearances', 'aerials_won']] = df_player_comp[['non_penalty_goals', 'npx_g', 'shots_total', 'assists', 'x_a', 'npx_g_plus_x_a', 'shot_creating_actions', 'passes_attempted', 'pass_completion_percent',
                       'progressive_passes', 'progressive_carries', 'dribbles_completed', 'touches_att_pen', 'progressive_passes_rec', 'pressures', 'tackles', 'interceptions', 'blocks',
                       'clearances', 'aerials_won']].apply(pd.to_numeric)
    
    categories = ['non_penalty_goals', 'npx_g', 'shots_total', 'assists', 'x_a', 'npx_g_plus_x_a', 'shot_creating_actions', 'passes_attempted', 'pass_completion_percent',
                       'progressive_passes', 'progressive_carries', 'dribbles_completed', 'touches_att_pen', 'progressive_passes_rec', 'pressures', 'tackles', 'interceptions', 'blocks',
                       'clearances', 'aerials_won']
    
    df_player_1_plot = [non_penalty_goals_x, npx_g_x, shots_total_x, assists_x, x_a_x, npx_g_plus_x_a_x, shot_creating_actions_x, passes_attempted_x, pass_completion_percent_x,
                       progressive_passes_x, progressive_carries_x, dribbles_completed_x, touches_att_pen_x, progressive_passes_rec_x, pressures_x, tackles_x, interceptions_x, blocks_x,
                       clearances_x, aerials_won_x]
    
    df_player_2_plot = [non_penalty_goals_y, npx_g_y, shots_total_y, assists_y, x_a_y, npx_g_plus_x_a_y, shot_creating_actions_y, passes_attempted_y, pass_completion_percent_y,
                       progressive_passes_y, progressive_carries_y, dribbles_completed_y, touches_att_pen_y, progressive_passes_rec_y, pressures_y, tackles_y, interceptions_y, blocks_y,
                       clearances_y, aerials_won_y]
    
    df_player_1_plot_numeric = []
    
    for item in df_player_1_plot:
        item = int(item)
        df_player_1_plot_numeric.append(item)
        
    df_player_2_plot_numeric = []
    
    for item in df_player_2_plot:
        item = int(item)
        df_player_2_plot_numeric.append(item)    
    
    N = 20
    
    angles = [n / float(N) * 2 * pi for n in range(N)]
    
    plt.figure(figsize=(40,10))
    
    ax = plt.subplot(111, polar=True)
    
    ax.set_theta_offset(pi / 2)
    
    ax.set_theta_direction(-1)
    
    plt.xticks(angles[:], categories)
    
    a = df_player_1_plot_numeric
    b = df_player_2_plot_numeric
    
    ax.plot(angles, a, linewidth=1, linestyle='solid', label=name_x, color ='grey')
    ax.fill(angles, a, 'b', alpha=0.3, color ='grey')
    
    ax.plot(angles, b, linewidth=1, linestyle='solid', label=name_y, color ='red')
    ax.fill(angles, b, 'b', alpha=0.3, color ='red')
    
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    
### Compare defensive stats for any two players


def compare_defensive_stats(x,y):
    
    warnings.filterwarnings("ignore")
    
    url_x = x
    url_y = y
    
    page_x =requests.get(url_x)
    page_y =requests.get(url_y)
    
    soup_x = BeautifulSoup(page_x.content, 'html.parser')
    soup_y = BeautifulSoup(page_y.content, 'html.parser')
    
    name_x = [element.text for element in soup_x.find_all("span")]
    name_y = [element.text for element in soup_y.find_all("span")]
    
    name_x = name_x[7]
    name_y = name_y[7]
    
    metric_names_x = []
    metric_names_y = []
    
    metric_values_x = []
    metric_values_y = []
    
    remove_content = ["'", "[", "]", ",", "%"]
    
    for row in soup_x.findAll('table')[0].tbody.findAll('tr'):
        first_column_x = row.findAll('th')[0].contents
        metric_names_x.append(first_column_x)
        
    for row in soup_y.findAll('table')[0].tbody.findAll('tr'):
        first_column_y = row.findAll('th')[0].contents
        metric_names_y.append(first_column_y)
        
    for row in soup_x.findAll('table')[0].tbody.findAll('tr'):
        first_column_x = row.findAll('td')[1].contents
        metric_values_x.append(first_column_x)
        
    for row in soup_y.findAll('table')[0].tbody.findAll('tr'):
        first_column_y = row.findAll('td')[1].contents
        metric_values_y.append(first_column_y)
        
    clean_left_x = []
    splitat_r = 65
    splitat_l = 67

    for item in metric_values_x:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_left_x.append(left)

    clean_overall_x = []
    
    for item in clean_left_x:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_overall_x.append(right)
    
    clean_x = []
    
    for item in clean_overall_x:
        item = item.replace("<","")
        clean_x.append(item)
        
    clean_left_y = []
    splitat_r = 65
    splitat_l = 67

    for item in metric_values_y:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_left_y.append(left)

    clean_overall_y = []
    
    for item in clean_left_y:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_overall_y.append(right)
    
    clean_y = []
    
    for item in clean_overall_y:
        item = item.replace("<","")
        clean_y.append(item)
        
    df_player_1 = pd.DataFrame()
    
    df_player_2 = pd.DataFrame()
    
    df_player_1['Name'] = name_x[0]
    df_player_1[metric_names_x[0]] = []
    df_player_1[metric_names_x[1]] = []
    df_player_1[metric_names_x[2]] = []
    df_player_1[metric_names_x[3]] = []
    df_player_1[metric_names_x[4]] = []
    df_player_1[metric_names_x[5]] = []
    df_player_1[metric_names_x[6]] = []
    df_player_1[metric_names_x[8]] = []
    df_player_1[metric_names_x[9]] = []
    df_player_1[metric_names_x[10]] = []
    df_player_1[metric_names_x[11]] = []
    df_player_1[metric_names_x[12]] = []
    df_player_1[metric_names_x[13]] = []
    df_player_1[metric_names_x[14]] = []
    df_player_1[metric_names_x[16]] = []
    df_player_1[metric_names_x[17]] = []
    df_player_1[metric_names_x[18]] = []
    df_player_1[metric_names_x[19]] = []
    df_player_1[metric_names_x[20]] = []
    df_player_1[metric_names_x[21]] = []
    
    df_player_2['Name'] = name_x[0]
    df_player_2[metric_names_y[0]] = []
    df_player_2[metric_names_y[1]] = []
    df_player_2[metric_names_y[2]] = []
    df_player_2[metric_names_y[3]] = []
    df_player_2[metric_names_y[4]] = []
    df_player_2[metric_names_y[5]] = []
    df_player_2[metric_names_y[6]] = []
    df_player_2[metric_names_y[8]] = []
    df_player_2[metric_names_y[9]] = []
    df_player_2[metric_names_y[10]] = []
    df_player_2[metric_names_y[11]] = []
    df_player_2[metric_names_y[12]] = []
    df_player_2[metric_names_y[13]] = []
    df_player_2[metric_names_y[14]] = []
    df_player_2[metric_names_y[16]] = []
    df_player_2[metric_names_y[17]] = []
    df_player_2[metric_names_y[18]] = []
    df_player_2[metric_names_y[19]] = []
    df_player_2[metric_names_y[20]] = []
    df_player_2[metric_names_y[21]] = []
    
    df_player_1 = kb.clean_column_names(df_player_1)
    df_player_2 = kb.clean_column_names(df_player_2)
        
    name_x = name_x
    non_penalty_goals_x = (clean_x[0])
    npx_g_x = clean_x[1]
    shots_total_x = clean_x[2]
    assists_x = clean_x[3]
    x_a_x = clean_x[4]
    npx_g_plus_x_a_x = clean_x[5] 
    shot_creating_actions_x = clean_x[6] 
    passes_attempted_x = clean_x[8] 
    pass_completion_percent_x = clean_x[9] 
    progressive_passes_x = clean_x[10] 
    progressive_carries_x = clean_x[11] 
    dribbles_completed_x = clean_x[12] 
    touches_att_pen_x = clean_x[13]
    progressive_passes_rec_x = clean_x[14] 
    pressures_x = clean_x[16] 
    tackles_x = clean_x[17] 
    interceptions_x = clean_x[18] 
    blocks_x = clean_x[19]
    clearances_x = clean_x[20]
    aerials_won_x = clean_x[21]
    
    df_player_1.loc[0] = [name_x, non_penalty_goals_x, npx_g_x, shots_total_x, assists_x, x_a_x, npx_g_plus_x_a_x, shot_creating_actions_x, passes_attempted_x, pass_completion_percent_x,
                       progressive_passes_x, progressive_carries_x, dribbles_completed_x, touches_att_pen_x, progressive_passes_rec_x, pressures_x, tackles_x, interceptions_x, blocks_x,
                       clearances_x, aerials_won_x]
    
    name_y = name_y
    non_penalty_goals_y = (clean_y[0])
    npx_g_y = clean_y[1]
    shots_total_y = clean_y[2]
    assists_y = clean_y[3]
    x_a_y = clean_y[4]
    npx_g_plus_x_a_y = clean_y[5] 
    shot_creating_actions_y = clean_y[6] 
    passes_attempted_y = clean_y[8] 
    pass_completion_percent_y = clean_y[9] 
    progressive_passes_y = clean_y[10] 
    progressive_carries_y = clean_y[11] 
    dribbles_completed_y = clean_y[12] 
    touches_att_pen_y = clean_y[13]
    progressive_passes_rec_y = clean_y[14] 
    pressures_y = clean_y[16] 
    tackles_y = clean_y[17] 
    interceptions_y = clean_y[18] 
    blocks_y = clean_y[19]
    clearances_y = clean_y[20]
    aerials_won_y = clean_y[21]
    
    df_player_2.loc[0] = [name_y, non_penalty_goals_y, npx_g_y, shots_total_y, assists_y, x_a_y, npx_g_plus_x_a_y, shot_creating_actions_y, passes_attempted_y, pass_completion_percent_y,
                       progressive_passes_y, progressive_carries_y, dribbles_completed_y, touches_att_pen_y, progressive_passes_rec_y, pressures_y, tackles_y, interceptions_y, blocks_y,
                       clearances_y, aerials_won_y]
    
    df_player_comp = pd.concat([df_player_1, df_player_2])
    
    df_player_defensive_comp = df_player_comp[['name','pressures', 'tackles', 'interceptions', 'blocks',
                       'clearances', 'aerials_won']]
    
    df_player_defensive_comp_plot = pd.DataFrame(index=np.arange(12), columns=np.arange(2))
    
    df_player_defensive_comp_plot.rename(columns={df_player_defensive_comp_plot.columns[0]: "Percentile" }, inplace = True)
    
    df_player_defensive_comp_plot.rename(columns={df_player_defensive_comp_plot.columns[1]: "Metric" }, inplace = True)
    
    player_name = [(df_player_defensive_comp_plot.index >= 0) & (df_player_defensive_comp_plot.index < 6),
         (df_player_defensive_comp_plot.index >= 6)]

    player_name_paste = [name_x, name_y]

    df_player_defensive_comp_plot['Player'] = np.select(player_name, player_name_paste)
    
    
    average_x = [int(pressures_x), int(tackles_x), int(interceptions_x), int(blocks_x),
                       int(clearances_x), int(aerials_won_x)]
    average_x = np.mean(average_x)
    
    
    average_y = [int(pressures_y), int(tackles_y), int(interceptions_y), int(blocks_y),
                       int(clearances_y), int(aerials_won_y)]
    average_y = np.mean(average_y)
    
    df_player_defensive_comp_plot.at[0, 'Metric'] = 'Pressures'
    df_player_defensive_comp_plot.at[1, 'Metric'] = 'Tackles'
    df_player_defensive_comp_plot.at[2, 'Metric'] = 'Interceptions'
    df_player_defensive_comp_plot.at[3, 'Metric'] = 'Blocks'
    df_player_defensive_comp_plot.at[4, 'Metric'] = 'Clearances'
    df_player_defensive_comp_plot.at[5, 'Metric'] = 'Ariels Won'
    df_player_defensive_comp_plot.at[7, 'Metric'] = 'Pressures'
    df_player_defensive_comp_plot.at[8, 'Metric'] = 'Tackles'
    df_player_defensive_comp_plot.at[9, 'Metric'] = 'Interceptions'
    df_player_defensive_comp_plot.at[10, 'Metric'] = 'Blocks'
    df_player_defensive_comp_plot.at[11, 'Metric'] = 'Clearances'
    df_player_defensive_comp_plot.at[12, 'Metric'] = 'Ariels Won'

    
    df_player_defensive_comp_plot.at[0, 'Percentile'] = int(pressures_x)
    df_player_defensive_comp_plot.at[1, 'Percentile'] = int(tackles_x)
    df_player_defensive_comp_plot.at[2, 'Percentile'] = int(interceptions_x)
    df_player_defensive_comp_plot.at[3, 'Percentile'] = int(blocks_x)
    df_player_defensive_comp_plot.at[4, 'Percentile'] = int(clearances_x)
    df_player_defensive_comp_plot.at[5, 'Percentile'] = int(aerials_won_x)
    df_player_defensive_comp_plot.at[7, 'Percentile'] = int(pressures_y)
    df_player_defensive_comp_plot.at[8, 'Percentile'] = int(tackles_y)
    df_player_defensive_comp_plot.at[9, 'Percentile'] = int(interceptions_y)
    df_player_defensive_comp_plot.at[10, 'Percentile'] = int(blocks_y)
    df_player_defensive_comp_plot.at[11, 'Percentile'] = int(clearances_y)
    df_player_defensive_comp_plot.at[12, 'Percentile'] = int(aerials_won_y)
    
    df_player_defensive_comp_plot = df_player_defensive_comp_plot[['Player', 'Metric', 'Percentile']]
    
    ax = sb.catplot(x = 'Player', y = 'Percentile', data = df_player_defensive_comp_plot, hue='Metric', s = 16, height=7, aspect=1)
    
    ax.set(ylim=(0, 100))

    la = {0: [average_x, name_x]}
    la_2 = {0: [average_y, name_y]}

    axes = ax.axes.flatten()

    for i, ax in enumerate(axes):
        ax.axhline(la[i][0], ls='--', c='green')
        
    for i, ax in enumerate(axes):
        ax.axhline(la_2[i][0], ls='--', c='purple')
        
    ax.text(0, average_x, name_x, transform=ax.transData)  
    ax.text(1, average_y, name_y, transform=ax.transData)  
    
    print(name_x,"is in the following percentile for defensive performance:",round(average_x,2))
    print(name_y, "is in the following percentile for defensive performance:",round(average_y,2))
    
    
### Compare offensive stats for any two players


def compare_offensive_stats(x,y):
    
    warnings.filterwarnings("ignore")
    
    url_x = x
    url_y = y
    
    page_x =requests.get(url_x)
    page_y =requests.get(url_y)
    
    soup_x = BeautifulSoup(page_x.content, 'html.parser')
    soup_y = BeautifulSoup(page_y.content, 'html.parser')
    
    name_x = [element.text for element in soup_x.find_all("span")]
    name_y = [element.text for element in soup_y.find_all("span")]
    
    name_x = name_x[7]
    name_y = name_y[7]
    
    metric_names_x = []
    metric_names_y = []
    
    metric_values_x = []
    metric_values_y = []
    
    remove_content = ["'", "[", "]", ",", "%"]
    
    for row in soup_x.findAll('table')[0].tbody.findAll('tr'):
        first_column_x = row.findAll('th')[0].contents
        metric_names_x.append(first_column_x)
        
    for row in soup_y.findAll('table')[0].tbody.findAll('tr'):
        first_column_y = row.findAll('th')[0].contents
        metric_names_y.append(first_column_y)
        
    for row in soup_x.findAll('table')[0].tbody.findAll('tr'):
        first_column_x = row.findAll('td')[1].contents
        metric_values_x.append(first_column_x)
        
    for row in soup_y.findAll('table')[0].tbody.findAll('tr'):
        first_column_y = row.findAll('td')[1].contents
        metric_values_y.append(first_column_y)
        
    clean_left_x = []
    splitat_r = 65
    splitat_l = 67

    for item in metric_values_x:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_left_x.append(left)

    clean_overall_x = []
    
    for item in clean_left_x:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_overall_x.append(right)
    
    clean_x = []
    
    for item in clean_overall_x:
        item = item.replace("<","")
        clean_x.append(item)
        
    clean_left_y = []
    splitat_r = 65
    splitat_l = 67

    for item in metric_values_y:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_left_y.append(left)

    clean_overall_y = []
    
    for item in clean_left_y:
        item = str(item).strip('[]')
        left, right = item[:splitat_l], item[splitat_r:]
        clean_overall_y.append(right)
    
    clean_y = []
    
    for item in clean_overall_y:
        item = item.replace("<","")
        clean_y.append(item)
        
    df_player_1 = pd.DataFrame()
    
    df_player_2 = pd.DataFrame()
    
    df_player_1['Name'] = name_x[0]
    df_player_1[metric_names_x[0]] = []
    df_player_1[metric_names_x[1]] = []
    df_player_1[metric_names_x[2]] = []
    df_player_1[metric_names_x[3]] = []
    df_player_1[metric_names_x[4]] = []
    df_player_1[metric_names_x[5]] = []
    df_player_1[metric_names_x[6]] = []
    df_player_1[metric_names_x[8]] = []
    df_player_1[metric_names_x[9]] = []
    df_player_1[metric_names_x[10]] = []
    df_player_1[metric_names_x[11]] = []
    df_player_1[metric_names_x[12]] = []
    df_player_1[metric_names_x[13]] = []
    df_player_1[metric_names_x[14]] = []
    df_player_1[metric_names_x[16]] = []
    df_player_1[metric_names_x[17]] = []
    df_player_1[metric_names_x[18]] = []
    df_player_1[metric_names_x[19]] = []
    df_player_1[metric_names_x[20]] = []
    df_player_1[metric_names_x[21]] = []
    
    df_player_2['Name'] = name_x[0]
    df_player_2[metric_names_y[0]] = []
    df_player_2[metric_names_y[1]] = []
    df_player_2[metric_names_y[2]] = []
    df_player_2[metric_names_y[3]] = []
    df_player_2[metric_names_y[4]] = []
    df_player_2[metric_names_y[5]] = []
    df_player_2[metric_names_y[6]] = []
    df_player_2[metric_names_y[8]] = []
    df_player_2[metric_names_y[9]] = []
    df_player_2[metric_names_y[10]] = []
    df_player_2[metric_names_y[11]] = []
    df_player_2[metric_names_y[12]] = []
    df_player_2[metric_names_y[13]] = []
    df_player_2[metric_names_y[14]] = []
    df_player_2[metric_names_y[16]] = []
    df_player_2[metric_names_y[17]] = []
    df_player_2[metric_names_y[18]] = []
    df_player_2[metric_names_y[19]] = []
    df_player_2[metric_names_y[20]] = []
    df_player_2[metric_names_y[21]] = []
    
    df_player_1 = kb.clean_column_names(df_player_1)
    df_player_2 = kb.clean_column_names(df_player_2)
        
    name_x = name_x
    non_penalty_goals_x = (clean_x[0])
    npx_g_x = clean_x[1]
    shots_total_x = clean_x[2]
    assists_x = clean_x[3]
    x_a_x = clean_x[4]
    npx_g_plus_x_a_x = clean_x[5] 
    shot_creating_actions_x = clean_x[6] 
    passes_attempted_x = clean_x[8] 
    pass_completion_percent_x = clean_x[9] 
    progressive_passes_x = clean_x[10] 
    progressive_carries_x = clean_x[11] 
    dribbles_completed_x = clean_x[12] 
    touches_att_pen_x = clean_x[13]
    progressive_passes_rec_x = clean_x[14] 
    pressures_x = clean_x[16] 
    tackles_x = clean_x[17] 
    interceptions_x = clean_x[18] 
    blocks_x = clean_x[19]
    clearances_x = clean_x[20]
    aerials_won_x = clean_x[21]
    
    df_player_1.loc[0] = [name_x, non_penalty_goals_x, npx_g_x, shots_total_x, assists_x, x_a_x, npx_g_plus_x_a_x, shot_creating_actions_x, passes_attempted_x, pass_completion_percent_x,
                       progressive_passes_x, progressive_carries_x, dribbles_completed_x, touches_att_pen_x, progressive_passes_rec_x, pressures_x, tackles_x, interceptions_x, blocks_x,
                       clearances_x, aerials_won_x]
    
    name_y = name_y
    non_penalty_goals_y = (clean_y[0])
    npx_g_y = clean_y[1]
    shots_total_y = clean_y[2]
    assists_y = clean_y[3]
    x_a_y = clean_y[4]
    npx_g_plus_x_a_y = clean_y[5] 
    shot_creating_actions_y = clean_y[6] 
    passes_attempted_y = clean_y[8] 
    pass_completion_percent_y = clean_y[9] 
    progressive_passes_y = clean_y[10] 
    progressive_carries_y = clean_y[11] 
    dribbles_completed_y = clean_y[12] 
    touches_att_pen_y = clean_y[13]
    progressive_passes_rec_y = clean_y[14] 
    pressures_y = clean_y[16] 
    tackles_y = clean_y[17] 
    interceptions_y = clean_y[18] 
    blocks_y = clean_y[19]
    clearances_y = clean_y[20]
    aerials_won_y = clean_y[21]
    
    df_player_2.loc[0] = [name_y, non_penalty_goals_y, npx_g_y, shots_total_y, assists_y, x_a_y, npx_g_plus_x_a_y, shot_creating_actions_y, passes_attempted_y, pass_completion_percent_y,
                       progressive_passes_y, progressive_carries_y, dribbles_completed_y, touches_att_pen_y, progressive_passes_rec_y, pressures_y, tackles_y, interceptions_y, blocks_y,
                       clearances_y, aerials_won_y]
    
    df_player_comp = pd.concat([df_player_1, df_player_2])
    
    df_player_offensive_comp = df_player_comp[['name', 'non_penalty_goals', 'npx_g', 'shots_total', 'assists', 'x_a', 'npx_g_plus_x_a', 'shot_creating_actions', 'pass_completion_percent',
                                              'progressive_passes', 'progressive_carries', 'dribbles_completed', 'touches_att_pen']]
    
    df_player_offensive_comp_plot = pd.DataFrame(index=np.arange(24), columns=np.arange(2))
    
    df_player_offensive_comp_plot.rename(columns={df_player_offensive_comp_plot.columns[0]: "Percentile" }, inplace = True)
    
    df_player_offensive_comp_plot.rename(columns={df_player_offensive_comp_plot.columns[1]: "Metric" }, inplace = True)
    
    player_name = [(df_player_offensive_comp_plot.index >= 0) & (df_player_offensive_comp_plot.index < 12),
         (df_player_offensive_comp_plot.index >= 12)]

    player_name_paste = [name_x, name_y]

    df_player_offensive_comp_plot['Player'] = np.select(player_name, player_name_paste)
    
    
    average_x = [int(non_penalty_goals_x), int(npx_g_x), int(shots_total_x), int(assists_x),
                       int(x_a_x), int(npx_g_plus_x_a_x), int(shot_creating_actions_x), int(pass_completion_percent_x), int(progressive_passes_x),
                int(progressive_carries_x), int(dribbles_completed_x), int(touches_att_pen_x)]
    average_x = np.mean(average_x)
    
    
    average_y = [int(non_penalty_goals_y), int(npx_g_y), int(shots_total_y), int(assists_y),
                       int(x_a_y), int(npx_g_plus_x_a_y), int(shot_creating_actions_y), int(pass_completion_percent_y), int(progressive_passes_y),
                int(progressive_carries_y), int(dribbles_completed_y), int(touches_att_pen_y)]
    average_y = np.mean(average_y)
    
    df_player_offensive_comp_plot.at[0, 'Metric'] = 'Non_penalty_goals'
    df_player_offensive_comp_plot.at[1, 'Metric'] = 'Npx_g'
    df_player_offensive_comp_plot.at[2, 'Metric'] = 'Shots_total'
    df_player_offensive_comp_plot.at[3, 'Metric'] = 'Assists'
    df_player_offensive_comp_plot.at[4, 'Metric'] = 'X_a'
    df_player_offensive_comp_plot.at[5, 'Metric'] = 'Npx_g_plus_x_a'
    df_player_offensive_comp_plot.at[6, 'Metric'] = 'Shot_creating_actions'
    df_player_offensive_comp_plot.at[7, 'Metric'] = 'Pass_completion_percent'
    df_player_offensive_comp_plot.at[8, 'Metric'] = 'Progressive_passes'
    df_player_offensive_comp_plot.at[9, 'Metric'] = 'Progressive_carries'
    df_player_offensive_comp_plot.at[10, 'Metric'] = 'Dribbles_completed'
    df_player_offensive_comp_plot.at[11, 'Metric'] = 'Touches_att_pen'
    df_player_offensive_comp_plot.at[12, 'Metric'] = 'Non_penalty_goals'
    df_player_offensive_comp_plot.at[13, 'Metric'] = 'Npx_g'
    df_player_offensive_comp_plot.at[14, 'Metric'] = 'Shots_total'
    df_player_offensive_comp_plot.at[15, 'Metric'] = 'Assists'
    df_player_offensive_comp_plot.at[16, 'Metric'] = 'X_a'
    df_player_offensive_comp_plot.at[17, 'Metric'] = 'Npx_g_plus_x_a'
    df_player_offensive_comp_plot.at[18, 'Metric'] = 'Shot_creating_actions'
    df_player_offensive_comp_plot.at[19, 'Metric'] = 'Pass_completion_percent'
    df_player_offensive_comp_plot.at[20, 'Metric'] = 'Progressive_passes'
    df_player_offensive_comp_plot.at[21, 'Metric'] = 'Progressive_carries'
    df_player_offensive_comp_plot.at[22, 'Metric'] = 'Dribbles_completed'
    df_player_offensive_comp_plot.at[23, 'Metric'] = 'Touches_att_pen'
    
    
    df_player_offensive_comp_plot.at[0, 'Percentile'] = int(non_penalty_goals_x)
    df_player_offensive_comp_plot.at[1, 'Percentile'] = int(npx_g_x)
    df_player_offensive_comp_plot.at[2, 'Percentile'] = int(shots_total_x)
    df_player_offensive_comp_plot.at[3, 'Percentile'] = int(assists_x)
    df_player_offensive_comp_plot.at[4, 'Percentile'] =  int(x_a_x)
    df_player_offensive_comp_plot.at[5, 'Percentile'] = int(npx_g_plus_x_a_x)
    df_player_offensive_comp_plot.at[6, 'Percentile'] = int(shot_creating_actions_x)
    df_player_offensive_comp_plot.at[7, 'Percentile'] = int(pass_completion_percent_x)
    df_player_offensive_comp_plot.at[8, 'Percentile'] = int(progressive_passes_x)
    df_player_offensive_comp_plot.at[9, 'Percentile'] = int(progressive_carries_x)
    df_player_offensive_comp_plot.at[10, 'Percentile'] =  int(dribbles_completed_x)
    df_player_offensive_comp_plot.at[11, 'Percentile'] = int(touches_att_pen_x)
    df_player_offensive_comp_plot.at[12, 'Percentile'] = int(non_penalty_goals_y)
    df_player_offensive_comp_plot.at[13, 'Percentile'] = int(npx_g_y)
    df_player_offensive_comp_plot.at[14, 'Percentile'] = int(shots_total_y)
    df_player_offensive_comp_plot.at[15, 'Percentile'] = int(assists_y)
    df_player_offensive_comp_plot.at[16, 'Percentile'] =  int(x_a_y)
    df_player_offensive_comp_plot.at[17, 'Percentile'] = int(npx_g_plus_x_a_y)
    df_player_offensive_comp_plot.at[18, 'Percentile'] = int(shot_creating_actions_y)
    df_player_offensive_comp_plot.at[19, 'Percentile'] = int(pass_completion_percent_y)
    df_player_offensive_comp_plot.at[20, 'Percentile'] = int(progressive_passes_y)
    df_player_offensive_comp_plot.at[21, 'Percentile'] = int(progressive_carries_y)
    df_player_offensive_comp_plot.at[22, 'Percentile'] =  int(dribbles_completed_y)
    df_player_offensive_comp_plot.at[23, 'Percentile'] = int(touches_att_pen_y)
    
    df_player_offensive_comp_plot = df_player_offensive_comp_plot[['Player', 'Metric', 'Percentile']]
    
    ax = sb.catplot(x = 'Player', y = 'Percentile', data = df_player_offensive_comp_plot, hue='Metric', s = 16, height=7, aspect=1)
    
    ax.set(ylim=(0, 100))

    la = {0: [average_x, name_x]}
    la_2 = {0: [average_y, name_y]}

    axes = ax.axes.flatten()

    for i, ax in enumerate(axes):
        ax.axhline(la[i][0], ls='--', c='green')
        
    for i, ax in enumerate(axes):
        ax.axhline(la_2[i][0], ls='--', c='purple')
        
    ax.text(0, average_x, name_x, transform=ax.transData)  
    ax.text(1, average_y, name_y, transform=ax.transData)  
    
    print(name_x,"is in the following percentile for defensive performance:",round(average_x,2))
    print(name_y, "is in the following percentile for defensive performance:",round(average_y,2))