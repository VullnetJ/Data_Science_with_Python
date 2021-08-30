  import pandas as myCutePandas
    import numpy as NumPy_is_here
    open_xml_file = myCutePandas.ExcelFile('Energy Indicators.xls')
    energy = open_xml_file.parse(skiprows=17,skip_footer=(38))
    e = energy[['Unnamed: 1',
                '%',
                'Gigajoules',
                'Petajoules'
                ]]
    e.columns = ['Country', 
                 'Energy Supply', 
                 'Energy Supply per Capita', 
                 '% Renewable']
    e[['Energy Supply', 
       'Energy Supply per Capita', 
       '% Renewable']] =  e[['Energy Supply', 
                             'Energy Supply per Capita', 
                             '% Renewable']].replace('...',NumPy_is_here.NaN).apply(myCutePandas.to_numeric)
    e['Energy Supply'] = e['Energy Supply']*1000000
    e['Country'] = e['Country'].replace({'Switzerland17':'Switzerland',
                                                   'Bolivia (Plurinational State of)':'Bolivia',
                                                   'Republic of Korea':'South Korea',
                                                   'United States of America':'United States',
                                                   'China, Hong Kong Special Administrative Region':'Hong Kong',
                                                   'United Kingdom of Great Britain and Northern Ireland':'United Kingdom',
                                                   'Republic of Korea':'South Korea',   
                                                   'Iran (Islamic Republic of)':'Iran'})
    e['Country'] = e['Country'].str.replace(r" \(.*\)","")  
    GDP = myCutePandas.read_csv('world_bank.csv',skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace('Korea, Rep.',
                                                      'South Korea')
    GDP['Country Name'] = GDP['Country Name'].replace('Iran, Islamic Rep.',
                                                      'Iran')
    GDP['Country Name'] = GDP['Country Name'].replace('Hong Kong SAR, China',
                                                      'Hong Kong')
    G = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    G.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    ScimEn = myCutePandas.read_excel(io='scimagojr-3.xlsx')
    slicing_ScimEn = ScimEn[:15]
    data_frames = myCutePandas.merge(slicing_ScimEn,e,right_on='Country',left_on='Country', how='inner')
    definitive_dataframe = myCutePandas.merge(data_frames,G, right_on='Country', left_on='Country', how='inner')
    definitive_dataframe = definitive_dataframe.set_index('Country')
    return definitive_dataframe
answer_one()

def answer_two():
    return 156

answer_two()
def answer_three():
    Top15 = answer_one()
    avgGDP = Top15[['2006',
                             '2007',
                             '2008',
                             '2009',
                             '2010',
                             '2011',
                             '2012',
                             '2013',
                             '2014',
                             '2015']].mean(axis=1).sort_values(ascending=False)
    return avgGDP
answer_three()

def answer_four():
    Top15 = answer_one()
    import pandas as superPandas
    difference = Top15[Top15['Rank'] == 4] ['2015'] 
    - Top15[Top15['Rank'] == 4]['2006']
    return superPandas.to_numeric(difference)[0]
answer_four()

def answer_five():
    Top15 = answer_one()
    Energy_Supply_per_Capita = Top15['Energy Supply per Capita'].mean()
    return Energy_Supply_per_Capita
answer_five()

def answer_six():
    Top15 = answer_one()
    max_Renewable_in_percent = Top15[Top15['% Renewable'] == max(Top15['% Renewable'])]
    return (max_Renewable_in_percent.index.tolist()[0],max_Renewable_in_percent['% Renewable'].tolist()[0])
answer_six()  

def answer_seven():
    Top15 = answer_one()
    Top15['country_with_highest_Citation_Ratio'] = Top15['Self-citations']/Top15['Citations']
    ratio_of_Self_Citations_to_Total_Citations = Top15[Top15['country_with_highest_Citation_Ratio'] == max(Top15['country_with_highest_Citation_Ratio'])]
    return (ratio_of_Self_Citations_to_Total_Citations.index.tolist()[0],ratio_of_Self_Citations_to_Total_Citations['country_with_highest_Citation_Ratio'].tolist()[0])
answer_seven() 

def answer_eight():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['Population'] = Top15['Population'].sort_values(ascending=True)
    return 'United States ', Top15['Population']
answer_eight() 

def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    number_of_citable_documents_per_person = Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
    return number_of_citable_documents_per_person

answer_nine()
def answer_ten():
    Top15 = answer_one()
    Top15['HighRenew'] = [1 if value_is_at_or_above_median >= Top15['% Renewable'].median() else 0 for value_is_at_or_above_median in Top15['% Renewable']]
    return Top15['HighRenew']
answer_ten()

def answer_eleven():
    Top15 = answer_one()
    import numpy as Numerical_Python
    import pandas as wowPandas
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15['PopEst'] = (Top15['Energy Supply'] / 
                       Top15['Energy Supply per Capita']).astype(float)
    Top15 = Top15.reset_index()
    Top15['Continent'] = [ContinentDict[name_of_the_country] for name_of_the_country in Top15['Country']]
    Continent = Top15.set_index('Continent').groupby(level=0)['PopEst'].agg({'size': Numerical_Python.size, 'sum': Numerical_Python.sum, 'mean': Numerical_Python.mean,'std': Numerical_Python.std})
    Continent = Continent[['size', 'sum', 'mean', 'std']]
    return Continent

answer_eleven()

def answer_twelve():
    Top15 = answer_one()
    import numpy as N
    import pandas as P
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    The_top15_with_resetted_index = Top15.reset_index()
    The_top15_with_resetted_index['Continent'] = [ContinentDict[name] for name in The_top15_with_resetted_index['Country']]
    The_top15_with_resetted_index['bins'] = P.cut(The_top15_with_resetted_index['% Renewable'],5)
    return The_top15_with_resetted_index.groupby(['Continent','bins']).size()
answer_twelve()

def answer_thirteen():
    Top15 = answer_one()
    import locale
    import pandas as pandpand
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    Top15['PopEst'] = (Top15['Energy Supply'] / Top15['Energy Supply per Capita']).astype(float)
    map_str = []
    for num in Top15['PopEst']:
        map_str.append(locale.format('%.2f',num,grouping=True))
    Top15['PopEst_str'] = map_str
    return Top15['PopEst_str']

answer_thirteen()