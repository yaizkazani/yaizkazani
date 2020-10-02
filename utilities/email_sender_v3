def send_email(to_emails, subject, body_text="", cc_emails=[], att_file=[]):
    """
    :param to_emails:  - list of recepients
    :param subject:  - email subject
    :param body_text:  - main text (optional)
    :param cc_emails:  - list of cc recepients (optional)
    :param att_file:  - list of strings of paths of file attachments (optional)
    :return:
    """
    import smtplib
    import os
    import configparser
    import sys
    import pathlib
    from email import encoders
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.utils import formatdate

    config_file_name = "config.ini"
    config_file_path = os.path.dirname(os.path.abspath(__file__)) + f"\{config_file_name}"

    ######################################################################################

    if not os.path.exists(config_file_path):  # checking if config exists
        print("Config file not found, exiting")
        sys.exit(1)
    else:
        conf = configparser.ConfigParser()  # create ConfigParser object
        conf.read(config_file_path)  # read config file
        try:
            smtp_server, from_addr, password, auth = conf.get("config", "server"), conf.get("config",
                                                                                            "account"), conf.get(
                "config", "password"), conf.get("config", "auth")  # get data from config
        except:
            print(
                "Cannot read config file. Config file should look like: \n[config]\nserver = servername\naccount = accountname\npassword = password\nauth = True(False)")
            sys.exit(1)
    msg = MIMEMultipart()  # create MIMEMultipart container - it will be used to keep our data
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    msg["To"] = ", ".join(to_emails)
    msg["cc"] = ", ".join(cc_emails)  # ↑ setting some parameters for our container

    if body_text:
        msg.attach(MIMEText(body_text))  # attaching body text if needed
    if att_file:
        for item in att_file:
            att_file_path = item
            attachment = MIMEBase("application", "octet-stream")  # creating MIMIBase object for attachment
            header = 'Content-Disposition', 'attachment; filename="%s"' % pathlib.Path(
                att_file_path).name  # creating header
            if os.path.exists(att_file_path):
                try:
                    with open(att_file_path, mode="rb") as att_file:  # rb = read binary
                        data = att_file.read()  # read file
                        attachment.set_payload(data)  # put data to container
                        encoders.encode_base64(attachment)  # encode it
                        attachment.add_header(*header)  # add header
                        msg.attach(attachment)  # attach to mail container
                except:
                    print("Error occured")
                    sys.exit(f"failed to add file {att_file_path}")
            else:
                print(f"Warning ! {att_file_path} was not found ! ")

    emails = to_emails + cc_emails
    server = smtplib.SMTP(smtp_server, 587)  # create smtp object

    if auth:  # if we use authentication
        server.starttls()  # starting TLS
        try:
            server.login(f"{from_addr}",
                         f"{password}")  # If doesnt work - google might block "unsafe" apps - need to enable it
        except smtplib.SMTPAuthenticationError:
            print("Cannot login to server")
            sys.exit(1)
    try:
        result = server.sendmail(from_addr, emails, msg.as_string())
        if result != {}:
            print(f"There was an error: {result}")
    except:
        print("Cannot send email, sendmail error")
        sys.exit(1)
    finally:
        server.quit()

# send_email(["yaizkazani@gmail.com"], "This is a test email from function", "test_email", att_file=[r"C:\Users\yaizk\Desktop\to_delete\1.txt", r"C:\Users\yaizk\Desktop\to_delete\test.txt"])
