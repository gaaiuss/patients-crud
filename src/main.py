from rich import print
from rich.markdown import Markdown

type Patient = dict[str, int | str]


def register_patient(patient_list: list[Patient]) -> None:
    name = input("Nome do paciente: ")

    try:
        age = int(input("Idade: "))
    except ValueError:
        print("\nPor favor digite uma idade válida!")
        return

    phone = input("Telefone: ")

    patient_list.append(
        {
            "nome": name,
            "idade": age,
            "telefone": phone,
        },
    )

    print("\nPaciente cadastrado com sucesso!")


def average_patient_age(patient_list: list[Patient]) -> int:
    age_sum = 0

    if len(patient_list) <= 1:
        return int(patient_list[0]["idade"])

    for patient in patient_list:
        age_sum += int(patient["idade"])

    return round(age_sum / 2)


def get_younger_patient(patient_list: list[Patient]) -> None:
    younger = patient_list[0]

    for patient in patient_list:
        if int(patient["idade"]) < int(younger["idade"]):
            younger = patient

    print("Nome do paciente mais novo:", younger["nome"], "- Idade:", younger["idade"])


def get_older_patient(patient_list: list[Patient]) -> None:
    older = patient_list[0]

    for patient in patient_list:
        if int(patient["idade"]) > int(older["idade"]):
            older = patient

    print("Nome do paciente mais velho:", older["nome"], "- Idade:", older["idade"])


def show_statistics(patient_list: list[Patient]) -> None:
    print("Número de pacientes cadastrados:", len(patient_list))
    print("Idade média dos pacientes:", average_patient_age(patient_list))
    get_younger_patient(patient_list)
    get_older_patient(patient_list)


def search_patient_by_name(patient_list: list[Patient]) -> None:
    patient_name = input("Digite o nome do paciente: ")
    for patient in patient_list:
        if patient_name == patient["nome"]:
            print("\nDados do paciente:\n")
            print("Nome:", patient["nome"])
            print("Idade:", patient["idade"])
            print("Telefone:", patient["telefone"])
            return

    print("Paciente não encontrado!")


def main() -> None:
    patient_list: list[Patient] = []

    while True:
        print(Markdown("---"))
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        print(Markdown("---"))

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("\nEscolha apenas números!")
            continue

        match option:
            case 1:
                print(Markdown("---"))
                register_patient(patient_list)
            case 2:
                print(Markdown("---"))
                show_statistics(patient_list)
            case 3:
                print(Markdown("---"))
                search_patient_by_name(patient_list)
            case 4:
                print(Markdown("---"))
                print("Pacientes\n")

                for patient in patient_list:
                    print("Nome do paciente: ", patient["nome"])
                    print("Idade: ", patient["idade"])
                    print("Telefone: ", patient["telefone"])
                    print()
            case 5:
                print("\nSaindo...")
                break
            case _:
                print("\nOpção inválida!")


if __name__ == "__main__":
    main()
