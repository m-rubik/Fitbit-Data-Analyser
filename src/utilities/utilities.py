import os

def write_to_master(category):
    try:
        filepath = './Data/'+category+'/Master.txt'
        if os.path.exists(filepath):
            os.remove(filepath) 
        with open(filepath, 'w') as outfile:
            for file in os.listdir('./Data/' + category + "/"):
                if file.endswith(".json"):
                    with open('./Data/' + category + "/" + file) as infile:
                        for line in infile:
                            outfile.write(line)
                    print(file,'copy to Master.txt complete.')
    except Exception as e:
        print(e)

def read_from_file(filename):
    try:
        filepath = './Data/'+filename
        if os.path.exists(filepath):
            text =''
            for line in open(filepath,"r", encoding='utf-8'):
                text += line
            print('Reading from',filename,'complete.')
            return text
        else:
            raise Exception("Path to file cannot be found.")
    except Exception as e:
        print(e)