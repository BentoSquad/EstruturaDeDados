import csv

def read_csv(file_path):
    """Leitura do arquivo CSV e passa linha por linha."""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row  # Passa cada linha do CSV como um dicionário


def age_filter(input_pipe):
    """Filtra clientes com idade maior ou igual a 18 anos."""
    for row in input_pipe:
        if int(row['idade']) >= 18:
            yield row  # Passa apenas clientes com 18 anos ou mais

def uppercase_name_filter(input_pipe):
    """Converte o nome do cliente para maiúsculas."""
    for row in input_pipe:
        row['nome'] = row['nome'].upper()  # Converte o nome para maiúsculas
        yield row  # Passa o cliente com o nome modificado


def lowercase_email_filter(input_pipe):
    """Formata o e-mail do cliente para minúsculas."""
    for row in input_pipe:
        row['email'] = row['email'].lower()  # Converte o e-mail para minúsculas
        yield row  # Passa o cliente com o e-mail formatado


def output_result(input_pipe):
    """Exibe o resultado final dos clientes filtrados e formatados."""
    for row in input_pipe:
        print(f"Nome: {row['nome']}, Email: {row['email']}, Idade: {row['idade']}")



if __name__ == "__main__":
    file_path = 'Implementacao\clientes.csv'  # Caminho do arquivo CSV de entrada
    
    # Pipeline: Conectar os filtros
    input_pipe = read_csv(file_path)
    age_filtered_pipe = age_filter(input_pipe)
    uppercase_name_pipe = uppercase_name_filter(age_filtered_pipe)
    formatted_email_pipe = lowercase_email_filter(uppercase_name_pipe)
    
    # Exibe o resultado
    output_result(formatted_email_pipe)
