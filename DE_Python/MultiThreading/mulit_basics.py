import threading
from concurrent.futures import ThreadPoolExecutor

def transform(input):
    src = input['src']
    dest = input['dest']

    print(f"Reading from: {src}")
    print("Transforming...")
    print(f"Writing data to: {dest}")

    return f"Done {src} to {dest}"



def main():
    array = [{"src":"table_1", "dest":"table_1"},
             {"src":"table_2", "dest":"table_2"},
             {"src":"table_3", "dest":"table_3"},
             {"src":"table_4", "dest":"table_4"},
             {"src":"table_5", "dest":"table_5"},
             {"src":"table_6", "dest":"table_6"},
             {"src":"table_7", "dest":"table_7"},
             {"src":"table_8", "dest":"table_8"},
             {"src":"table_9", "dest":"table_9"},
             {"src":"table_10", "dest":"table_10"},
             {"src":"table_11", "dest":"table_11"},
             {"src":"table_12", "dest":"table_12"}]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        my_futures = executor.map(transform, array)
        print(list(my_futures))

if __name__ == '__main__':
    main()

    
    
    
