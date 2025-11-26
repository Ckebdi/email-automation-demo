import imaplib
import email
import os
from email.header import decode_header

# --- CONFIGURATION (EXEMPLE) ---
# Dans un projet réel, utilisez des variables d'environnement pour la sécurité
USERNAME = "contact@example.com"
PASSWORD = "password123"
IMAP_SERVER = "ssl0.ovh.net" # Exemple pour OVH comme cité dans votre CV
ATTACHMENT_DIR = "./pieces_jointes_extraites"

def connect_to_email():
    """Établit la connexion sécurisée au serveur IMAP."""
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(USERNAME, PASSWORD)
        return mail
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return None

def process_emails(mail):
    """Parcourt les emails et extrait les factures/pièces jointes."""
    mail.select("INBOX")
    
    # Recherche des emails non lus contenant 'Facture' dans le sujet
    status, messages = mail.search(None, '(UNSEEN SUBJECT "Facture")')
    email_ids = messages[0].split()

    print(f"{len(email_ids)} emails trouvés à traiter.")

    for email_id in email_ids:
        # Récupération de l'email
        res, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                
                print(f"Traitement de : {subject}")
                
                # Extraction des pièces jointes
                for part in msg.walk():
                    if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is None:
                        continue
                        
                    filename = part.get_filename()
                    if filename:
                        filepath = os.path.join(ATTACHMENT_DIR, filename)
                        # Sauvegarde feinte (pour la démo)
                        print(f" -> Pièce jointe détectée : {filename} (Sauvegarde...)")
                        # with open(filepath, "wb") as f: f.write(part.get_payload(decode=True))

if __name__ == "__main__":
    # Simulation du workflow
    print("--- Démarrage du Script d'Automatisation ---")
    # mail = connect_to_email()
    # if mail:
    #     process_emails(mail)
    #     mail.logout()
    print("Code de démonstration : connexion et logique implémentées.")
