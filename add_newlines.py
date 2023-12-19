def reformat_credentials(filename):
    """
  Reformatiert jede Zeile der Datei von 'email:passwort | Country = ...' zu 'Mail: email\nPasswort: passwort\n\n'.

  Args:
    filename: Der Name der Eingabedatei.

  Returns:
    Eine neue Datei mit umformatierten Zeilen.

  @ChrisHaSaar - 12/2023
  """

    # Dateinamensuffix vor der Dateierweiterung einfügen
    filename_out = filename.replace('.txt', '_neuformatiert.txt')

    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename_out, "w") as f_out:
        for line in lines:
            parts = line.strip().split(' | ')
            email_part, password_part = parts[0].split(':')
            email = email_part.strip()
            password = password_part.strip()
            f_out.write(f"Mail: {email}\nPasswort: {password}\n\n")

    print("Neu formatierte Datei gespeichert als:", filename_out)


if __name__ == "__main__":
    filename = input("Quelldatei: ")
    reformat_credentials(filename)
