"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    import pandas as pd
    with open("files/input/clusters_report.txt", "r") as file:
        data = {"cluster": [], "cantidad_de_palabras_clave": [], "porcentaje_de_palabras_clave": [], "principales_palabras_clave": []}

        for line in file.readlines()[4:]:
            line = line.replace("\n", "")
            data_in_file = list(filter(lambda x: x != "", line.split(" ")))

            if "%" in data_in_file:
                data["cluster"].append(int(data_in_file[0]))
                data["cantidad_de_palabras_clave"].append(int(data_in_file[1]))
                data["porcentaje_de_palabras_clave"].append(float(data_in_file[2].replace(",", ".")))
                data["principales_palabras_clave"].append(" ".join(data_in_file[4:]).replace(".", "").strip() + " ")
            elif data_in_file:
                data["principales_palabras_clave"][-1] += " ".join(data_in_file).replace(".", "").strip() + " "

        # Eliminar el espacio al final de cada cadena de palabras clave
        data["principales_palabras_clave"] = list(map(lambda x: x.strip(), data["principales_palabras_clave"]))

        df = pd.DataFrame(data)

    return df

print(pregunta_01())
