import pandas as pd
import json_lines

def read_data_from_jl(file_path):
    with open(file_path, 'rb') as f:
        data = json_lines.reader(f)

        df = pd.DataFrame(data)
        
        return df
    return None


if __name__ == '__main__':
    df = read_data_from_jl('prices.jl')
    for e in df.values[:,0].reshape((-1,1)):
        print(e)
    print((df.values[:,0] == 'Thỏa thuận').sum(), len(df.values))
    
    