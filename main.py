"""
Crée des instances de User, Admin et Ticket, affiche leurs propriétés et
invoque chaque méthode du diagramme de classes au moins une fois.
"""
from datetime import date

from user import User
from admin import Admin
from ticket import Ticket


def titre(texte: str) -> None:
    print()
    print("=" * 60)
    print(texte)
    print("=" * 60)


def afficher_user(u: User) -> None:
    print(f"User   : userID={u.userID}, name='{u.name}', "
          f"email='{u.email}', role='{u.role}'")


def afficher_admin(a: Admin) -> None:
    print(f"Admin  : adminID={a.adminID}, name='{a.name}', email='{a.email}'")


def afficher_ticket(t: Ticket) -> None:
    print(f"Ticket : ticketID={t.ticketID}, title='{t.title}', "
          f"description='{t.description}', status='{t.status}', "
          f"priority='{t.priority}', creationDate={t.creationDate}, "
          f"updateDate={t.updateDate}")


def main() -> None:
    # ------------------------------------------------------------------
    titre("1. Création des objets")
    # ------------------------------------------------------------------
    aujourd_hui = date.today()

    user1 = User(1, "Abdoul Zongo", "Abdoul@uqac.ca", "Développeuse")
    user2 = User(2, "Isma Ky", "Isma@uqac.ca", "Testeur")
    admin = Admin(100, "Miky COD", "carole@uqac.ca")

    ticket1 = Ticket(
        ticketID=1,
        title="Bug de connexion",
        description="Impossible de se connecter avec un mot de passe valide",
        status="Ouvert",
        priority="Haute",
        creationDate=aujourd_hui,
        updateDate=aujourd_hui,
    )
    ticket2 = Ticket(
        ticketID=2,
        title="Erreur d'affichage",
        description="Le tableau de bord ne s'affiche pas sur mobile",
        status="Ouvert",
        priority="Moyenne",
        creationDate=aujourd_hui,
        updateDate=aujourd_hui,
    )
    ticket3 = Ticket(
        ticketID=3,
        title="Demande de fonctionnalité",
        description="Ajouter un export CSV des tickets",
        status="Nouveau",
        priority="Basse",
        creationDate=aujourd_hui,
        updateDate=aujourd_hui,
    )
    print("Objets créés : 2 User, 1 Admin, 3 Tickets")

    # ------------------------------------------------------------------
    titre("2. Propriétés des objets créés")
    # ------------------------------------------------------------------
    afficher_user(user1)
    afficher_user(user2)
    afficher_admin(admin)
    afficher_ticket(ticket1)
    afficher_ticket(ticket2)
    afficher_ticket(ticket3)

    # ------------------------------------------------------------------
    titre("3. Méthodes de User")
    # ------------------------------------------------------------------
    print("\n--- User.createTicket(ticket) ---")
    user1.createTicket(ticket1)
    user1.createTicket(ticket2)
    user2.createTicket(ticket3)
    print(f"Résultat : {user1.name} a créé "
          f"{[t.ticketID for t in user1.createdTickets]}, "
          f"{user2.name} a créé {[t.ticketID for t in user2.createdTickets]}")

    print("\n--- User.viewTicket(ticket) ---")
    user1.viewTicket(ticket1)
    user2.viewTicket(ticket3)
    print(f"Résultat : {user1.name} a consulté "
          f"{[t.ticketID for t in user1.viewedTickets]}, "
          f"{user2.name} a consulté {[t.ticketID for t in user2.viewedTickets]}")

    print("\n--- User.updateTicket(ticket) ---")
    user1.updateTicket(ticket2)
    print("Résultat : ", end="")
    afficher_ticket(ticket2)

    # ------------------------------------------------------------------
    titre("4. Méthodes de Ticket")
    # ------------------------------------------------------------------
    print("\n--- Ticket.updateStatus(status) ---")
    ticket1.updateStatus("En cours")
    #ticket1.updateStatus("Terminé")

    print("Résultat : ", end="")
    afficher_ticket(ticket1)

    print("\n--- Ticket.addComment(comment) ---")
    ticket1.addComment("Reproduit sur l'environnement de test.")
    print("Résultat : ", end="")
    afficher_ticket(ticket1)

    print("\n--- Ticket.assignTo(user) (appel direct) ---")
    ticket3.assignTo(user2)
    print("Résultat : ", end="")
    afficher_ticket(ticket3)

    # ------------------------------------------------------------------
    titre("5. Méthodes de Admin")
    # ------------------------------------------------------------------
    print("\n--- Admin.assignTicket(ticket, user) ---")
    admin.assignTicket(ticket1, user1)
    admin.assignTicket(ticket2, user2)
    print(f"Résultat : tickets assignés par {admin.name} = "
          f"{[t.ticketID for t in admin.assignedTickets]}")

    print("\n--- Admin.closeTicket(ticket) ---")
    admin.closeTicket(ticket1)
    print("Résultat : ", end="")
    afficher_ticket(ticket1)

    print("\n--- Admin.viewAllTickets() ---")
    tickets = admin.viewAllTickets()
    print(f"Résultat : liste de {len(tickets)} ticket(s) retournée")
    for t in tickets:
        print("    ", end="")
        afficher_ticket(t)

    # ------------------------------------------------------------------
    titre("6. État final de tous les tickets")
    # ------------------------------------------------------------------
    for t in (ticket1, ticket2, ticket3):
        afficher_ticket(t)


if __name__ == "__main__":
    main()
