from proyecto_integrador.proyect import Proyect
from proyecto_integrador.organization import Organization
from proyecto_integrador.responsible import Responsible

def hub():
    organization = Organization("GreenTech Global", None, [])
    while True:
        print("\nMenú Principal")
        print("1 - Crear un nuevo proyecto")
        print("2 - Mostrar información de un proyecto")
        print("3 - Actualizar el estado de un proyecto")
        print("4 - Ordenar proyectos por emisiones reducidas")
        print("5 - Calcular total de emisiones reducidas")
        print("6 - Determinar proyectos completados")
        print("7 - Salir")

        option = input("Seleccione una opción: ")
        if option == "1":
            id = input("ID del proyecto: ")
            name = input("Nombre del proyecto: ")
            type = input("Tipo de energía (solar, eólica, etc.): ")
            location = input("Ubicación: ")
            dni = input("DNI del responsable: ")
            name_responsible = input("Nombre del responsable: ")
            last_name_responsible = input("Apellido del responsable: ")
            email = input("Email del responsable: ")
            phone = input("Teléfono del responsable: ")
            responsible = Responsible(dni, name_responsible, last_name_responsible, email, phone)
            reductions_emissions = float(input("Emisiones reducidas (en toneladas): "))
            energy_regeneration = float(input("Energía generada (en kWh): "))
            status = input("Estado del proyecto (pendiente, en curso, completado): ")
            proyect = Proyect(id, name, type, location, responsible, reductions_emissions, energy_regeneration, status)
            organization.proyects.append(proyect)

            print("Proyecto agregado exitosamente.")

        elif option == "2":

            id = input("ID del proyecto a mostrar: ")
            proyect = next((p for p in organization.proyects if p.get_id() == id), None)

            if proyect:
                print(f"ID: {proyect.get_id()}")
                print(f"Nombre: {proyect.name}")
                print(f"Tipo: {proyect.type}")
                print(f"Ubicación: {proyect.get_location()}")
                responsible = proyect.get_responsible()
                print(f"Responsable: {responsible.name} {responsible.last_name}")
                print(f"Emisiones Reducidas: {proyect.reductions_emissions} toneladas")
                print(f"Energía Generada: {proyect.energy_regeneration} kWh")
                print(f"Estado: {proyect.status}")
                
            else:
                print("Proyecto no encontrado.")

        elif option == "3":
            id = input("ID del proyecto a actualizar: ")
            proyect = next((p for p in organization.projects if p.get_id() == id), None)

            if proyect:
                new_status = input("Nuevo estado del proyecto (pendiente, en curso, completado): ")
                proyect.status = new_status
                print("Estado actualizado exitosamente.")

            else:
                print("Proyecto no encontrado.")

        elif option == "4":
            projects = sorted(organization.projects, key=lambda p: p.reductions_emissions, reverse=True)
            for p in projects:
                print(f"{p.name} - {p.reductions_emissions} toneladas")

        elif option == "5":
            total_emissions = sum(p.reductions_emissions for p in organization.projects)
            print(f"Total de emisiones reducidas: {total_emissions} toneladas")
            
        elif option == "6":
            completed_projects = len([p for p in organization.projects if p.status == "completado"])
            print(f"Proyectos completados: {completed_projects}")

        elif option == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    hub()