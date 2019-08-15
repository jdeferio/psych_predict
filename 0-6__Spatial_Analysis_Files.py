import pandas as pd

spatial_data = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/maindataOct192018_4_FIPS.csv', encoding='utf-8')

def spatial_files(df):

    output_filepath1 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/spatial_400m.csv'
    output_filepath2 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/spatial_800m.csv'
    output_filepath3 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/spatial_1600m.csv'

    cols_400m = [col for col in spatial_data.columns if '400' in col]
    cols_800m = [col for col in spatial_data.columns if '800' in col]
    cols_1600m = [col for col in spatial_data.columns if '1600' in col]

    fips = spatial_data['fips_census_code']
    spatial_400 = spatial_data[cols_400m]
    spatial_800 = spatial_data[cols_800m]
    spatial_1600 = spatial_data[cols_1600m]

    spatial_400m = pd.concat([fips,spatial_400],axis=1)
    spatial_800m = pd.concat([fips, spatial_800], axis=1)
    spatial_1600m = pd.concat([fips, spatial_1600], axis=1)

    pd.DataFrame(spatial_400m).to_csv(output_filepath1, encoding='utf-8')
    pd.DataFrame(spatial_800m).to_csv(output_filepath2, encoding='utf-8')
    pd.DataFrame(spatial_1600m).to_csv(output_filepath3, encoding='utf-8')

spatial_files(spatial_data)


