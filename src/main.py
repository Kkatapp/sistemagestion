import queries
from pipline import process
import queries

def main():
    df = queries.count_patients()
    print(df)
    
if __name__ == "__main__":
    main()