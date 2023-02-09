# PROJET DE DISTRIBUTION DES DONS ET AIDES AUX PERSONNES

### DESCRIPTION DU PROJET 

Ce projet développé par <a href = "github.com/TonyV23">HAKIZMANA Tony Carlin</a>, facilite la gestion de distribution des dons et aides aux personnes vulnérables de la population burundaise .

### CE QUE PEUT FAIRE AVEC CE SITE WEB

Ce site est conçu pour fonctioner au sein d'une fondation qui s'occupe des personnes vulnérables en leur distribuant des aides et dons provenant soit de la part de la fondation elle même ou de la part de donateurs .

### LES ACTEURS DU PROJET

- ###### Les personnes vulnérables qui sont identifiées par :
    * le nom et prénom
    * la date de naissance et le sexe
    * le nom et prénom du père et de la mère
    * la province, la commune et la zone d'origine
    * sa situation de vulnérabilite
    * son niveau d'études
    * son statut matrimonial
    * le nombre d'enfants à sa charge
    * la fonction occupée
    * la date d'enregistrement

- ###### Les donateurs qui sont identifiés par :
    * le type ou la catégorie du donateur 
    * le type d'aide 
    * le type d'assistance
    * le montant
    * le numéro de téléphone
    * l'adresse mail
    * la déscription du don ou d'aides
    * la date de donation   
### LES DIFFERENTES FONCTIONNALITES :

- ###### gestion des utilisateurs du site :
    * Le système a deux groupes :
        
        -- le groupe "admins" qui contient les utilisateurs qui ont tous les droits d'accès .
        
        -- le groupe "employees" qui contient les utilisateurs qui ont les droits de CRUD seulement 
            sur les tables de distribution , donateurs et personnes .

    * Le super utilisateur du système qui a le rôle d'admin crée de nouveaux utilisateurs qui sont 
        automatiquement ajoutés dans le groupe des employés .

    * Pour l'authentification le système analyse quel type de groupe l'utilisateur se trouve et le  redirige vers les pages auxquelles il a le droit d'accès grâce aux décorateurs .

    * Le système de gestion des mots de passe :
        - En cas d'oublie du mot de passe l'utilisateur a droit de réinitialiser son mot de passe en faisant une demande d'un lien vers de réinitialisation

        - Comme l'admin est celui qui crée de nouveaux utilisateurs, une fois créée l'utilisateur a la possibilité de changer son mot de passe     
- ###### gestion des personnes vulnérables : 
    * Enregistrement, affichage, modification , suppression et recherche des informations sur les personnes vulnérables de la base des données

- ###### gestion des donateurs : 
    * Enregistrement, affichage, modification , suppression et recherche des informations les donateurs de la base des données

- ###### gestion des distributions des dons : 
    * Enregistrement, affichage, modification , suppression et recherche des informations les distributions des dons

- ###### gestion des provinces et collines : 
    * Enregistrement, affichage, modification , suppression et recherche des informations les provinces et collines

- ###### gestion de vulnérabilités, des niveaux d'études, des statuts matrimoniaux, des types aides et des types assistances: 
    * Enregistrement, affichage, modification , suppression et recherche des informations sur les vulnérabilités, les niveaux d'études, les statuts matrimoniaux, les types aides et les types assistances
- ###### consultation des statistiques sur :
    
    * Les origines des personnes vulnérables (voir quelle province compte le plus de personnes vulnérables)
    
    * Les vulnerabilités des personnes vulnérables (voir les vulnerabilités qui sont beaucoup présentes dans les camps enfin de déterminer quel type d'assistance les personnes vulnérables ont besoin)

    * Le niveau d'études des personnes vulnérables (aide dans la détermination le pourcentage du nombre des analphabètes, ceux (celles) qui ont un enseignement primaire, et ou secondaire / technique)

    * Le statut matrimonial matrimoniale (voir le pourcentage des personnes mariées, séparéés, célibataires, divorcées et veuves)

    * Le nombre total des femmes et des hommes

    * Les types de donateurs (voir si c'est sont des organisations, des entreprises, des associations, des particuliers ou des anonymes et leur nombre nombre de participations)

    * Le nombre de nouvelles personnes vulnérables par jour

    * Le nombre de bénéficiaires ayant reçu un don

### TECHNOLOGIES UTILISEES

- ###### FRONTED : 
    * Le framework bootstrap v4
- ###### BACKEND : 
    * Le framework Django v4.1 (autres package se trouvent dans le fichier requirements.txt )
- ###### BASE DE DONNEES : 
    * Le système de gestion des bases de données __MySQl__
- ###### MailTrap : 
    * Pour le service de réinitialisation des mots de passe des utilisateurs