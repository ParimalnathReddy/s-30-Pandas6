import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    dictionary = []
    for i in range(len(person)):
        pid = person['id'][i]
        email = person['email'][i]
        if email in dictionary:
            if pid < dictionary[email]:
                dictionary[email] = pid
        else:
            dictionary[email] = pid
    result = []
    for key,value in dictionary.item():
        result.append([value,key])
    return pd.DataFrame(result,columns= ['id','email'])
        
        
               
    