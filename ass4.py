 empty_list = []
    list_of_cities = None
    region = []
    with open('university_towns.txt') as document:
        for city in document:
            cities = city[:-1]
            if cities[-6:] == '[edit]':
                state = cities[:-6]
                continue
            if '(' in city:
                town = cities[:cities.index('(')-1]
                region.append([list_of_cities,town])
            else:
                town = cities
                region.append([list_of_cities,town])
            empty_list.append(cities)
    dataframe = pd.DataFrame(region,columns = ['State','RegionName'])
    return dataframe
get_list_of_university_towns()

    GDP_over_time = pd.ExcelFile('gdplev.xls')
    GDP_over_time = GDP_over_time.parse("Sheet1", skiprows=219)
    GDP_over_time = GDP_over_time[['1999q4', 9926.1]]
    GDP_over_time.columns = ['Quarter','GDP']
    for gdp in range(2, len(GDP_over_time)):
        if (GDP_over_time.iloc[gdp-2][1] > GDP_over_time.iloc[gdp-1][1]) and (GDP_over_time.iloc[gdp-1][1] > GDP_over_time.iloc[gdp][1]):
            return GDP_over_time.iloc[gdp-2][0]
get_recession_start()


GDP_over_time = pd.ExcelFile('gdplev.xls')
    GDP_over_time = GDP_over_time.parse("Sheet1", skiprows=219)
    GDP_over_time = GDP_over_time[['1999q4', 9926.1]]
    GDP_over_time.columns = ['Quarter','GDP']
    begining_of_recession = get_recession_start()
    begin = GDP_over_time[GDP_over_time['Quarter'] == begining_of_recession].index.tolist()[0]
    GDP_over_time=GDP_over_time.iloc[begin:]
    for value in range(2, len(GDP_over_time)):
        if (GDP_over_time.iloc[value-2][1] < GDP_over_time.iloc[value-1][1]) and (GDP_over_time.iloc[value-1][1] < GDP_over_time.iloc[value][1]):
            return GDP_over_time.iloc[value][0]  
get_recession_end()

bottom_recession = pd.ExcelFile('gdplev.xls')
    bottom_recession = bottom_recession.parse("Sheet1", skiprows=219)
    bottom_recession = bottom_recession[['1999q4', 9926.1]]
    bottom_recession.columns = ['Quarter','GDP']
    begin = get_recession_start()
    begin_line = bottom_recession[bottom_recession['Quarter'] == begin].index.tolist()[0]
    final = get_recession_end()
    final_line = bottom_recession[bottom_recession['Quarter'] == final].index.tolist()[0]
    bottom_recession=bottom_recession.iloc[begin_line:final_line+1]
    rec = bottom_recession['GDP'].min()
    rec_bottom = bottom_recession[bottom_recession['GDP'] == rec].index.tolist()[0]-begin_line
    return bottom_recession.iloc[rec_bottom]['Quarter']
get_recession_bottom()


reading_input = pd.read_csv('City_Zhvi_AllHomes.csv')
    reading_input = reading_input.drop(reading_input.columns[[0]+list(range(3,51))],axis=1)
    reading_second = pd.DataFrame(reading_input[['State','RegionName']])
    for year in range(2000,2016):
        reading_second[str(year)+'q1'] = reading_input[[str(year)+'-01',str(year)+'-02',str(year)+'-03']].mean(axis=1)
        reading_second[str(year)+'q2'] = reading_input[[str(year)+'-04',str(year)+'-05',str(year)+'-06']].mean(axis=1)
        reading_second[str(year)+'q3'] = reading_input[[str(year)+'-07',str(year)+'-08',str(year)+'-09']].mean(axis=1)
        reading_second[str(year)+'q4'] = reading_input[[str(year)+'-10',str(year)+'-11',str(year)+'-12']].mean(axis=1)
    year = 2016    
    reading_second[str(year)+'q1'] = reading_input[[str(year)+'-01',str(year)+'-02',str(year)+'-03']].mean(axis=1)
    reading_second[str(year)+'q2'] = reading_input[[str(year)+'-04',str(year)+'-05',str(year)+'-06']].mean(axis=1)
    reading_second[str(year)+'q3'] = reading_input[[str(year)+'-07',str(year)+'-08']].mean(axis=1)
    reading_second = reading_second.replace({'State':'states'})
    reading_second = reading_second.set_index(['State','RegionName'])
    return reading_second

convert_housing_data_to_quarters()

 list_of_uni = get_list_of_university_towns()
    recession_bottom = get_recession_bottom()
    recession_start = get_recession_start()
    
    convert_to_quarter = convert_housing_data_to_quarters()
    bstart = convert_to_quarter.columns[convert_to_quarter.columns.get_loc(recession_start) -1]
    
    convert_to_quarter['ratio'] = convert_to_quarter[recession_bottom] - convert_to_quarter[bstart]
    convert_to_quarter = convert_to_quarter[[recession_bottom, bstart,'ratio']]
    convert_to_quarter = convert_to_quarter.reset_index()
    
    unitowns_hdata = pd.merge(convert_to_quarter,list_of_uni,how='inner',on=['State','RegionName'])
    unitowns_hdata['uni'] = True
    
    convert_to_quarter2 = pd.merge(convert_to_quarter,unitowns_hdata,how='outer',on=['State','RegionName',recession_bottom,bstart,'ratio'])
    convert_to_quarter2['uni'] = convert_to_quarter2['uni'].fillna(False)
    
    ut = convert_to_quarter2[convert_to_quarter2['uni'] == True]
    nut = convert_to_quarter2[convert_to_quarter2['uni'] == False]
    t,p = ttest_ind(ut['ratio'].dropna(),nut['ratio'].dropna())
    different = True if p < 0.01 else False
    better = "non-university town" if ut['ratio'].mean() < nut['ratio'].mean() else "university town"
    return different, p, better

run_ttest()