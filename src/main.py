import queries

def main():
    paciente = queries.get_patient("PAT-09484753")
    print(paciente)
    
if __name__ == "__main__":
    main()