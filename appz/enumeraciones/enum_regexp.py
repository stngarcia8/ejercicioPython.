

class Exp:

    # Expresion regular aplicada al nombre.
    __parteNombre = "^([A-Za-zÑñ\-]{1,})"
    __parteApellidos = "\s([A-Za-zÑñ\-]{1,})[\s]{0,1}([A-Za-zÑñ\-]{0,})$"
    NOMBRE = __parteNombre+__parteApellidos

    # Expresion regular aplicada al rut.
    RUT = "^([0-9]+-[0-9Kk])$"

    # Expresion regular aplicada al eMail.
    __parteNombre = "^[+a-zA-Z0-9._-]+"
    __parteDominio = "@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"
    EMAIL = __parteNombre+__parteDominio

    # Expresion regular aplicada a campos numericos.
    NUMERO = "^[0-9]{1,}$"

    # Expresion regular aplicada a los campos codigos. hasta 6 caracteres.
    CODIGO = "^[0-9]{1,6}$"

    # Expresion regular para los campos de fecha.
    __parteDia1 = "^(?:(?:(?:0?[1-9]|1\d|2[0-8])[/]"
    __parteDia2 = "(?:0?[1-9]|1[0-2])|(?:29|30)[/](?:0?[13-9]|1[0-2])|31[/]"
    __parteMes1 = "(?:0?[13578]|1[02]))[/](?:0{2,3}[1-9]"
    __parteMes2 = "|0{1,2}[1-9]\d|0?[1-9]\d{2}"
    __parteAnio1 = "|[1-9]\d{3})|29[/]0?2[/](?:\d{1,2}(?:0[48]|[2468][048]"
    __parteAnio2 = "|[13579][26])|(?:0?[48]|[13579][26]|[2468][048])00))$"
    __dia = __parteDia1+__parteDia2
    __mes = __parteMes1+__parteMes2
    __anio = __parteAnio1+__parteAnio2
    FECHA = __dia+__mes+__anio
