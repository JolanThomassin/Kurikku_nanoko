from tkinter import*
import time
import random

class Jeux() :
	def __init__(self):
		### Paramètres ###
		self.LargeurEcran = 1080
		self.HauteurEcran = 720 
		self.EcranDeJeux = Tk()
		self.EcranDeJeux.title("Kurikku nanoko")
		self.EcranDeJeux.geometry("1080x720+200+40")
		self.EcranDeJeux.iconbitmap("miku.ico")
		self.EcranDeJeux.resizable(width=0, height=0)
		self.CanvaUn = Canvas(self.EcranDeJeux, width=self.LargeurEcran, height=self.HauteurEcran, bg="black")
		self.CanvaUn.pack()

		### Démarrage ###
		self.MenuAccueil()

		### Variables ###
		self.InGame = False
		self.argent = 0
		self.argentTotal = 0
		self.weeb = 0
		self.puissanceClique = 1

		### Waifu ###
		self.nombreWaifu = 0
		self.waifuUn = False

		### Cosmétique ###
		self.LunetteCommunPossession = False
		self.LunetteCommunÉquipé = False
		self.CasquetteCommunPossession = False
		self.CasquetteCommunÉquipé = False
		self.MasqueCommunPossession = False
		self.MasqueCommunÉquipé = False
		self.BoucleOreilleCommunPossession = False
		self.BoucleOreilleCommunÉquipé = False
		self.YeuxRougeRarePossession = False
		self.YeuxRougeRareÉquipé = False 
		self.ShibaRarePossession = False
		self.ShibaRareÉquipé = False
		self.TailsÉpiquePossession = False
		self.TailsÉpiqueÉquipé = False
		self.LégendairePossession = False
		self.LégendaireÉquipé = False

		### Caisse de Skin ###
		self.prixCaisse = 5000
		self.compteur = 0
		self.résultatPrécédent = random.randint(0, 99) 
		self.résultatActuel = random.randint(0, 99) 
		self.résulatSuivant = random.randint(0, 99)  
		self.résultatActuelString = ""
		self.couleurRésultatActuel = ""
		self.contenuCaisse = [
		"Lunette", "Lunette", "Lunette", "Lunette", "Lunette", "Lunette", "Lunette", "Lunette", "Lunette", "Lunette", 
		"Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", 
		"Masque", "Masque", "Masque", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", 
		"Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", 
		"Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", 
		"Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", 
		"Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", 
		"Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Shiba", "Shiba", "Shiba", "Shiba", 
		"Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", 
		"Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Légendaire"]

		### Lancement ###
		self.FonctionTimer()
		self.EcranDeJeux.mainloop() 

	def MenuAccueil(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Images ###
		self.BackgroundDécor = PhotoImage(file="salle/salleAccueil.png")
		self.CanvaUn.create_image(540, 360, image=self.BackgroundDécor)
		self.imageRessource = PhotoImage(file="boutonBoutique/boutonRessource.png")
		self.imageWaifu = PhotoImage(file="boutonBoutique/boutonWaifu.png")
		self.imageCaisse = PhotoImage(file="boutonBoutique/boutonCaisse.png")
		self.imageCollection = PhotoImage(file="boutonBoutique/boutonCollection.png")

		### Textes ###
		self.texteDébut = self.CanvaUn.create_text(545, 155, text= "Kurikku nanoko", font=("OCR A Extended", 50), fill="#AE0D1E")
		self.texteDébut2 = self.CanvaUn.create_text(540, 150, text= "Kurikku nanoko", font=("OCR A Extended", 50), fill="#CF3747")

		### Boutons ###
		self.boutonChargerPartie = Button(self.EcranDeJeux, text="  Charger partie  ", font=("OCR A Extended", 30), bg='white', fg='#A44040', command=self.ChargerLaPartie)
		self.boutonChargerPartie = self.CanvaUn.create_window(self.LargeurEcran/2, (self.HauteurEcran/2)-50, window=self.boutonChargerPartie)
		self.boutonNouvellePartie = Button(self.EcranDeJeux, text="  Nouvelle partie  ", font=("OCR A Extended", 30), bg='white', fg='#A44040', command=self.LancerTuto)
		self.boutonNouvellePartie = self.CanvaUn.create_window(self.LargeurEcran/2, (self.HauteurEcran/2)+50, window=self.boutonNouvellePartie)
		self.boutonMenuCrédit = Button(self.EcranDeJeux, text="  Crédit  ", font=("OCR A Extended", 25), bg='white', fg='#A44040', command=self.LancerCredit)
		self.boutonMenuCrédit = self.CanvaUn.create_window(self.LargeurEcran/2, (self.HauteurEcran/2)+150, window=self.boutonMenuCrédit)
		self.boutonMenuQuitter = Button(self.EcranDeJeux, text="  Quitter  ", font=("OCR A Extended", 25), bg='white', fg='#A44040', command=self.QuitterJeu)
		self.boutonMenuQuitter = self.CanvaUn.create_window(self.LargeurEcran/2, (self.HauteurEcran/2)+250, window=self.boutonMenuQuitter)

	def ChargerLaPartie(self):
		self.FenetrePrincipale()
		self.ChargerSauvegarde()

	def QuitterJeu(self):
		self.EcranDeJeux.destroy()

	def LancerCredit(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Textes ###
		self.texteFaitPar = self.CanvaUn.create_text(self.LargeurEcran/2, 203, text= "Réalisé par :", font=("OCR A Extended", 30), fill="#AE0D1E")
		self.texteFaitParDouble = self.CanvaUn.create_text(self.LargeurEcran/2, 200, text= "Réalisé par :", font=("OCR A Extended", 30), fill="#AE0D1E")
		self.texteJolanThomassin = self.CanvaUn.create_text(self.LargeurEcran/2, 303, text= "Jolan Thomassin", font=("OCR A Extended", 60), fill="#FF14E6")
		self.texteJolanThomassinDouble = self.CanvaUn.create_text(self.LargeurEcran/2, 300, text= "Jolan Thomassin", font=("OCR A Extended", 60), fill="#FBFF0F")

		### Boutons ###
		self.boutonMenuQuitter = Button(self.EcranDeJeux, text="  Retour  ", font=("OCR A Extended", 20), bg='white', fg='#A44040', command=self.MenuAccueil)
		self.boutonMenuQuitter = self.CanvaUn.create_window(self.LargeurEcran/2, self.LargeurEcran/1.70, window=self.boutonMenuQuitter)

	def GagnerArgent(self):
		self.argent = self.argent + self.puissanceClique
		self.argentTotal = self.argentTotal + self.puissanceClique
		self.ActualisationArgent()

	def FenetrePrincipale(self):
		### Reset ###
		self.CanvaUn.delete(ALL)
		self.InGame = True

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/bureau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Cosmétique ###
		if self.TailsÉpiqueÉquipé == True :
			self.cosmTailsEquipement = PhotoImage(file="cosmétique/cosmétiqueTailsÉpique.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-300, (self.HauteurEcran/2), image=self.cosmTailsEquipement)
		
		### Image ###
		if self.YeuxRougeRareÉquipé == True :
			self.cosmYeuxRougeEquipement = PhotoImage(file="cosmétique/cosmétiqueYeuxRougeRare.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2+50), image=self.cosmYeuxRougeEquipement)
		else :
			self.personnagePrincipale = PhotoImage(file="Mio Akiyama/waifuPersonnage.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.personnagePrincipale)
			
		### Cosmétique ###
		if self.BoucleOreilleCommunÉquipé == True :
			self.cosmBoucleOreilleEquipement = PhotoImage(file="cosmétique/cosmétiqueBoucleOreilleCommun.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.cosmBoucleOreilleEquipement) 
		if self.LunetteCommunÉquipé == True :
			self.cosmLunetteEquipement = PhotoImage(file="cosmétique/cosmétiqueLunetteCommun.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.cosmLunetteEquipement)
		if self.LégendaireÉquipé == True :
			self.cosmLégendaire = PhotoImage(file="cosmétique/cosmétiqueLégendaire.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.cosmLégendaire)
		if self.ShibaRareÉquipé == True :
			self.cosmShibaEquipement = PhotoImage(file="cosmétique/cosmétiqueShibaRare.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-50, (self.HauteurEcran/2)+200, image=self.cosmShibaEquipement)
		if self.CasquetteCommunÉquipé == True :
			self.cosmCasquetteEquipement = PhotoImage(file="cosmétique/cosmétiqueCasquetteCommun.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.cosmCasquetteEquipement)
		if self.MasqueCommunÉquipé == True :
			self.cosmMasqueCommunEquipement = PhotoImage(file="cosmétique/cosmétiqueMasqueCommun.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.cosmMasqueCommunEquipement)

		### Texte ###
		self.ArgentTextuel()
 
		### Boutons ###
		self.boutonQuête = Button(self.EcranDeJeux, text="Quête", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageQuête)
		self.boutonQuête = self.CanvaUn.create_window(835, 590, window=self.boutonQuête)
		self.boutonStats = Button(self.EcranDeJeux, text=" Stats ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuStats)
		self.boutonStats = self.CanvaUn.create_window(970, 590, window=self.boutonStats)
		self.boutonArgent = Button(self.EcranDeJeux, text=" Vendre des photos ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.GagnerArgent)
		self.boutonArgent = self.CanvaUn.create_window(self.LargeurEcran/2, 660, window=self.boutonArgent)
		self.boutonMenuSauvegarde = Button(self.EcranDeJeux, text=" Menu Sauvegarde ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuSauvegarde)
		self.boutonMenuSauvegarde = self.CanvaUn.create_window(200, 660, window=self.boutonMenuSauvegarde)
		self.boutonBoutique = Button(self.EcranDeJeux, text=" Boutique ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonBoutique = self.CanvaUn.create_window(820, 660, window=self.boutonBoutique) 
		self.boutonQuitter = Button(self.EcranDeJeux, text=" ❌ ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.QuitterJeu)
		self.boutonQuitter = self.CanvaUn.create_window(990, 660, window=self.boutonQuitter)

	def Sauvegarde(self):
		with open("sauvegarde.txt", "r") as fichier :
			lignes = fichier.readlines()
			lignes[0] = str(self.argent) + "\n"
			lignes[1] = str(self.argentTotal) + "\n"
			lignes[2] = str(self.weeb) + "\n"
			lignes[3] = str(self.nombreWaifu) + "\n"
			lignes[4] = str(self.waifuUn) + "\n"
			lignes[5] = str(self.puissanceClique) + "\n"
			lignes[6] = str(self.LunetteCommunPossession) + "\n"
			lignes[7] = str(self.LunetteCommunÉquipé) + "\n"
			lignes[8] = str(self.CasquetteCommunPossession) + "\n"
			lignes[9] = str(self.CasquetteCommunÉquipé) + "\n"
			lignes[10] = str(self.MasqueCommunPossession) + "\n"
			lignes[11] = str(self.MasqueCommunÉquipé) + "\n"
			lignes[12] = str(self.BoucleOreilleCommunPossession) + "\n"
			lignes[13] = str(self.BoucleOreilleCommunÉquipé) + "\n"
			lignes[14] = str(self.YeuxRougeRarePossession) + "\n"
			lignes[15] = str(self.YeuxRougeRareÉquipé) + "\n"
			lignes[16] = str(self.ShibaRarePossession) + "\n"
			lignes[17] = str(self.ShibaRareÉquipé) + "\n"
			lignes[18] = str(self.TailsÉpiquePossession) + "\n"
			lignes[19] = str(self.TailsÉpiqueÉquipé) + "\n"
			lignes[20] = str(self.LégendairePossession) + "\n"
			lignes[21] = str(self.LégendaireÉquipé) + "\n"
			lignes[22] = str(self.prixCaisse) + "\n"
		with open("sauvegarde.txt", "w") as fichier :
			fichier.writelines(lignes)

	def ChargerSauvegarde(self):
		with open("sauvegarde.txt", "r") as fichier :
			lignes = fichier.readlines()
			self.argent = int(lignes[0])
			self.argentTotal = int(lignes[1])
			self.weeb = int(lignes[2])
			self.nombreWaifu = int(lignes[3])
			self.waifuUn = str(lignes[4])
			if self.waifuUn == "False\n" :
				self.waifuUn = False
			else :
				self.waifuUn = True
			self.puissanceClique = int(lignes[5])
			self.LunetteCommunPossession = str(lignes[6])
			if self.LunetteCommunPossession == "False\n" :
				self.LunetteCommunPossession = False
			else :
				self.LunetteCommunPossession = True
			self.LunetteCommunÉquipé = str(lignes[7])
			if self.LunetteCommunÉquipé == "False\n" :
				self.LunetteCommunÉquipé = False
			else :
				self.LunetteCommunÉquipé = True

			self.CasquetteCommunPossession = str(lignes[8])
			if self.CasquetteCommunPossession == "False\n" :
				self.CasquetteCommunPossession = False
			else :
				self.CasquetteCommunPossession = True

			self.CasquetteCommunÉquipé = str(lignes[9])
			if self.CasquetteCommunÉquipé == "False\n" :
				self.CasquetteCommunÉquipé = False
			else :
				self.CasquetteCommunÉquipé = True

			self.MasqueCommunPossession = str(lignes[10])
			if self.MasqueCommunPossession == "False\n" :
				self.MasqueCommunPossession = False
			else :
				self.MasqueCommunPossession = True

			self.MasqueCommunÉquipé = str(lignes[11])
			if self.MasqueCommunÉquipé == "False\n" :
				self.MasqueCommunÉquipé = False
			else :
				self.MasqueCommunÉquipé = True

			self.BoucleOreilleCommunPossession = str(lignes[12])
			if self.BoucleOreilleCommunPossession == "False\n" :
				self.BoucleOreilleCommunPossession = False
			else :
				self.BoucleOreilleCommunPossession = True

			self.BoucleOreilleCommunÉquipé = str(lignes[13])
			if self.BoucleOreilleCommunÉquipé == "False\n" :
				self.BoucleOreilleCommunÉquipé = False
			else :
				self.BoucleOreilleCommunÉquipé = True

			self.YeuxRougeRarePossession = str(lignes[14])
			if self.YeuxRougeRarePossession == "False\n" :
				self.YeuxRougeRarePossession = False
			else :
				self.YeuxRougeRarePossession = True

			self.YeuxRougeRareÉquipé = str(lignes[15])
			if self.YeuxRougeRareÉquipé == "False\n" :
				self.YeuxRougeRareÉquipé = False
			else :
				self.YeuxRougeRareÉquipé = True

			self.ShibaRarePossession = str(lignes[16])
			if self.ShibaRarePossession == "False\n" :
				self.ShibaRarePossession = False
			else :
				self.ShibaRarePossession = True

			self.ShibaRareÉquipé = str(lignes[17])
			if self.ShibaRareÉquipé == "False\n" :
				self.ShibaRareÉquipé = False
			else :
				self.ShibaRareÉquipé = True

			self.TailsÉpiquePossession = str(lignes[18])
			if self.TailsÉpiquePossession == "False\n" :
				self.TailsÉpiquePossession = False
			else :
				self.TailsÉpiquePossession = True

			self.TailsÉpiqueÉquipé = str(lignes[19])
			if self.TailsÉpiqueÉquipé == "False\n" :
				self.TailsÉpiqueÉquipé = False
			else :
				self.TailsÉpiqueÉquipé = True

			self.LégendairePossession = str(lignes[20])
			if self.LégendairePossession == "False\n" :
				self.LégendairePossession = False
			else :
				self.LégendairePossession = True

			self.LégendaireÉquipé = str(lignes[21])
			if self.LégendaireÉquipé == "False\n" :
				self.LégendaireÉquipé = False
			else :
				self.LégendaireÉquipé = True

			self.prixCaisse = int(lignes[22])

		### Textes ###
		self.ActualisationArgent()

		### Reset ###
		self.FenetrePrincipale()

	def MenuStats(self):
		### Compteur ###
		nombreCosmetique = 0
		if self.LunetteCommunPossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.CasquetteCommunPossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.MasqueCommunPossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.BoucleOreilleCommunPossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.YeuxRougeRarePossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.ShibaRarePossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.TailsÉpiquePossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.LégendairePossession == True :
			nombreCosmetique = nombreCosmetique + 1

		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/stats.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Texte ###
		self.statsArgent = self.CanvaUn.create_text((self.LargeurEcran/2), 100, text= "Argent total :", font=("OCR A Extended", 30), fill="white")
		self.statsArgentDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 103, text= "Argent total :", font=("OCR A Extended", 30), fill="Grey")
		self.affichageArgentTotal = self.CanvaUn.create_text((self.LargeurEcran/2)+6, 146, text= self.argentTotal, font=("OCR A Extended", 30), fill="#1CF8FF")
		self.affichageArgentTotalDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 143, text= self.argentTotal, font=("OCR A Extended", 30), fill="#FF14E6")
		self.affichageArgentTotalTriple = self.CanvaUn.create_text(self.LargeurEcran/2, 140, text= self.argentTotal, font=("OCR A Extended", 30), fill="#FBFF0F")

		self.statsWeeb = self.CanvaUn.create_text((self.LargeurEcran/2), 200, text= "Weebs possédés :", font=("OCR A Extended", 30), fill="white")
		self.statsWeebDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 203, text= "Weebs possédés :", font=("OCR A Extended", 30), fill="Grey")
		self.afficheWeeb = self.CanvaUn.create_text((self.LargeurEcran/2)+6, 246, text= self.weeb, font=("OCR A Extended", 30), fill="#1CF8FF")
		self.afficheWeebDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 243, text= self.weeb, font=("OCR A Extended", 30), fill="#FF14E6")
		self.afficheWeebTriple = self.CanvaUn.create_text(self.LargeurEcran/2, 240, text= self.weeb, font=("OCR A Extended", 30), fill="#FBFF0F")

		self.statsNombreWaifu = self.CanvaUn.create_text((self.LargeurEcran/2), 300, text= "Waifu possédés :", font=("OCR A Extended", 30), fill="white")
		self.statsNombreWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 303, text= "Waifu possédés :", font=("OCR A Extended", 30), fill="Grey")
		self.afficheWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+6, 346, text= str(self.nombreWaifu) + "/1", font=("OCR A Extended", 30), fill="#1CF8FF")
		self.afficheWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 343, text= str(self.nombreWaifu) + "/1", font=("OCR A Extended", 30), fill="#FF14E6")
		self.afficheWaifuTriple = self.CanvaUn.create_text(self.LargeurEcran/2, 340, text= str(self.nombreWaifu) + "/1", font=("OCR A Extended", 30), fill="#FBFF0F")

		self.statsNombreCosmétique = self.CanvaUn.create_text((self.LargeurEcran/2), 400, text= "Cosmétique possédés :", font=("OCR A Extended", 30), fill="white")
		self.statsNombreCosmétiqueDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 403, text= "Cosmétique possédés :", font=("OCR A Extended", 30), fill="Grey")
		self.afficheCosmétique = self.CanvaUn.create_text((self.LargeurEcran/2)+6, 446, text= str(nombreCosmetique) + "/8", font=("OCR A Extended", 30), fill="#1CF8FF")
		self.afficheCosmétiqueDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 443, text= str(nombreCosmetique) + "/8", font=("OCR A Extended", 30), fill="#FF14E6")
		self.afficheCosmétiqueTriple = self.CanvaUn.create_text(self.LargeurEcran/2, 440, text= str(nombreCosmetique) + "/8", font=("OCR A Extended", 30), fill="#FBFF0F")

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 650, window=self.boutonRetour)

	def MenuSauvegarde(self):
		### Reset ###
		self.CanvaUn.delete(self.boutonMenuSauvegarde)

		### Boutons ###
		self.boutonChargerSauvegarde = Button(self.EcranDeJeux, text=" Charger sauvegarde ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.ChargerSauvegarde)
		self.boutonChargerSauvegarde = self.CanvaUn.create_window(200, 460, window=self.boutonChargerSauvegarde)
		self.boutonSauvegarde = Button(self.EcranDeJeux, text=" Sauvegarder ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.Sauvegarde)
		self.boutonSauvegarde = self.CanvaUn.create_window(200, 560, window=self.boutonSauvegarde)
		self.boutonFermerSauvegarde = Button(self.EcranDeJeux, text=" Fermer Menu ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonFermerSauvegarde = self.CanvaUn.create_window(200, 660, window=self.boutonFermerSauvegarde)

	def MenuBoutique(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/shop.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Boutons ###
		self.boutonDeGauche = Button(self.EcranDeJeux, image=self.imageRessource, command=self.Ressources, borderwidth=0)
		self.boutonDeGauche = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonDeGauche)
		self.boutonDeDroite = Button(self.EcranDeJeux, image=self.imageWaifu, command=self.pageWaifu, borderwidth=0)
		self.boutonDeDroite = self.CanvaUn.create_window(self.LargeurEcran/2+250, self.HauteurEcran/2, window=self.boutonDeDroite)

		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueDeuxième)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueDeuxième)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)

		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		self.texteGauche = self.CanvaUn.create_text(self.LargeurEcran/2-250, self.HauteurEcran/2+250, text= "Ressource", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteGaucheDouble = self.CanvaUn.create_text(self.LargeurEcran/2-247, self.HauteurEcran/2+247, text= "Ressource", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.texteDroite = self.CanvaUn.create_text(self.LargeurEcran/2+250, self.HauteurEcran/2+250, text= "Waifu", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteDroiteDouble = self.CanvaUn.create_text(self.LargeurEcran/2+247, self.HauteurEcran/2+247, text= "Waifu", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.ArgentTextuel()

	def MenuBoutiqueDeuxième(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/shop.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Boutons ###
		self.boutonDeGauche = Button(self.EcranDeJeux, image=self.imageCaisse, command=self.pageCaisse, borderwidth=0)
		self.boutonDeGauche = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonDeGauche)
		self.boutonDeDroite = Button(self.EcranDeJeux, image=self.imageCollection, command=self.pageCollection, borderwidth=0)
		self.boutonDeDroite = self.CanvaUn.create_window(self.LargeurEcran/2+250, self.HauteurEcran/2, window=self.boutonDeDroite)

		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)

		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		self.texteGauche = self.CanvaUn.create_text(self.LargeurEcran/2-250, self.HauteurEcran/2+250, text= "Caisse", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteGaucheDouble = self.CanvaUn.create_text(self.LargeurEcran/2-247, self.HauteurEcran/2+247, text= "Caisse", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.texteDroite = self.CanvaUn.create_text(self.LargeurEcran/2+250, self.HauteurEcran/2+250, text= "Collection", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteDroiteDouble = self.CanvaUn.create_text(self.LargeurEcran/2+247, self.HauteurEcran/2+247, text= "Collection", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.ArgentTextuel()

	def pageQuête(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		self.texteQuête = self.CanvaUn.create_text((self.LargeurEcran/2)+3, (self.HauteurEcran/2)+3, text= "À venir", font=("OCR A Extended", 100), fill="#FF14E6")
		self.texteQuêteDouble = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2, text= "À venir", font=("OCR A Extended", 100), fill="#FBFF0F")

	def pageCollection(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.imageDeCollection = PhotoImage(file="salle/pageCollection.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.imageDeCollection)
		self.imageIconeCaché = PhotoImage(file="cosmétique/iconeCaché.png")
		self.imageIconeLunette = PhotoImage(file="cosmétique/iconeLunette.png")
		self.imageIconeCasquette = PhotoImage(file="cosmétique/iconeCasquette.png")
		self.imageIconeBoucleOreille = PhotoImage(file="cosmétique/iconeBoucleOreille.png")
		self.imageIconeMasque = PhotoImage(file="cosmétique/iconeMasque.png")
		self.imageIconeYeuxRouge = PhotoImage(file="cosmétique/iconeYeuxRouge.png")
		self.imageIconeShiba = PhotoImage(file="cosmétique/iconeCasquette.png")
		self.imageIconeTails = PhotoImage(file="cosmétique/iconeTails.png")
		self.imageIconeShiba = PhotoImage(file="cosmétique/iconeShiba.png")
		self.imageIconeLégendaire = PhotoImage(file="cosmétique/iconeLégendaire.png")

		### Boutons ###
		if self.LunetteCommunPossession == True :
			self.boutonDeFullGaucheHaut = Button(self.EcranDeJeux, image=self.imageIconeLunette, command=self.EquipementLunette, borderwidth=2, highlightcolor="grey",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullGaucheHaut = self.CanvaUn.create_window(self.LargeurEcran/2-400, self.HauteurEcran/2-170, window=self.boutonDeFullGaucheHaut)
		else :		
			self.boutonDeFullGaucheHaut = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullGaucheHaut = self.CanvaUn.create_window(self.LargeurEcran/2-400, self.HauteurEcran/2-170, window=self.boutonDeFullGaucheHaut)
		if self.CasquetteCommunPossession == True :
			self.boutonGaucheHaut = Button(self.EcranDeJeux, image=self.imageIconeCasquette, command=self.EquipementCasquette, borderwidth=2, highlightcolor="grey",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonGaucheHaut = self.CanvaUn.create_window(self.LargeurEcran/2-135, self.HauteurEcran/2-170, window=self.boutonGaucheHaut)
		else :
			self.boutonGaucheHaut = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonGaucheHaut = self.CanvaUn.create_window(self.LargeurEcran/2-135, self.HauteurEcran/2-170, window=self.boutonGaucheHaut)
		if self.BoucleOreilleCommunPossession == True :
			self.boutonDeFullDroiteHaut = Button(self.EcranDeJeux, image=self.imageIconeBoucleOreille, command=self.EquipementBoucleOreille, borderwidth=2, highlightcolor="grey",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullDroiteHaut = self.CanvaUn.create_window(self.LargeurEcran/2+400, self.HauteurEcran/2-170, window=self.boutonDeFullDroiteHaut)
		else :
			self.boutonDeFullDroiteHaut = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullDroiteHaut = self.CanvaUn.create_window(self.LargeurEcran/2+400, self.HauteurEcran/2-170, window=self.boutonDeFullDroiteHaut)
		if self.MasqueCommunPossession == True :
			self.boutonDroiteHaut = Button(self.EcranDeJeux, image=self.imageIconeMasque, command=self.EquipementMasque, borderwidth=2, highlightcolor="grey",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDroiteHaut = self.CanvaUn.create_window(self.LargeurEcran/2+135, self.HauteurEcran/2-170, window=self.boutonDroiteHaut)
		else :
			self.boutonDroiteHaut = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDroiteHaut = self.CanvaUn.create_window(self.LargeurEcran/2+135, self.HauteurEcran/2-170, window=self.boutonDroiteHaut)
		
		if self.YeuxRougeRarePossession == True :
			self.boutonDeFullGaucheBas = Button(self.EcranDeJeux, image=self.imageIconeYeuxRouge, command=self.EquipementYeuxRouge, borderwidth=2, highlightcolor="aqua",highlightbackground="aqua",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullGaucheBas = self.CanvaUn.create_window(self.LargeurEcran/2-400, self.HauteurEcran/2+170, window=self.boutonDeFullGaucheBas)
		else :
			self.boutonDeFullGaucheBas = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullGaucheBas = self.CanvaUn.create_window(self.LargeurEcran/2-400, self.HauteurEcran/2+170, window=self.boutonDeFullGaucheBas)
		if self.ShibaRarePossession == True :
			self.boutonGaucheBas = Button(self.EcranDeJeux, image=self.imageIconeShiba, command=self.EquipementShiba, borderwidth=2, highlightcolor="aqua",highlightbackground="aqua",highlightthickness=5,relief=SOLID, default='active')
			self.boutonGaucheBas = self.CanvaUn.create_window(self.LargeurEcran/2-135, self.HauteurEcran/2+170, window=self.boutonGaucheBas)
		else :
			self.boutonGaucheBas = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonGaucheBas = self.CanvaUn.create_window(self.LargeurEcran/2-135, self.HauteurEcran/2+170, window=self.boutonGaucheBas)
		if self.TailsÉpiquePossession == True :
			self.boutonDroiteBas = Button(self.EcranDeJeux, image=self.imageIconeTails, command=self.EquipementTails, borderwidth=2, highlightcolor="purple",highlightbackground="purple",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDroiteBas = self.CanvaUn.create_window(self.LargeurEcran/2+135, self.HauteurEcran/2+170, window=self.boutonDroiteBas)
		else :
			self.boutonDroiteBas = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDroiteBas = self.CanvaUn.create_window(self.LargeurEcran/2+135, self.HauteurEcran/2+170, window=self.boutonDroiteBas)
		if self.LégendairePossession == True :
			self.boutonDeFullDroiteBas = Button(self.EcranDeJeux, image=self.imageIconeLégendaire, command=self.EquipementDrip, borderwidth=2, highlightcolor="yellow",highlightbackground="yellow",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullDroiteBas = self.CanvaUn.create_window(self.LargeurEcran/2+400, self.HauteurEcran/2+170, window=self.boutonDeFullDroiteBas)
		else :
			self.boutonDeFullDroiteBas = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullDroiteBas = self.CanvaUn.create_window(self.LargeurEcran/2+400, self.HauteurEcran/2+170, window=self.boutonDeFullDroiteBas)

		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueDeuxième)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		self.confirmationEquipement = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2, text= "", font=("OCR A Extended", 30), fill="black")

	def EquipementLunette(self):
		if self.LunetteCommunÉquipé == True :
			self.LunetteCommunÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Lunette déséquipé")
		else : 
			self.LunetteCommunÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Lunette équipé")

	def EquipementCasquette(self):
		if self.CasquetteCommunÉquipé == True :
			self.CasquetteCommunÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Casquette déséquipé")
		else : 
			self.CasquetteCommunÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Casquette équipé")

	def EquipementBoucleOreille(self):
		if self.BoucleOreilleCommunÉquipé == True :
			self.BoucleOreilleCommunÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Boucle d'oreilles déséquipé")
		else : 
			self.BoucleOreilleCommunÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Boucle d'oreilles équipé")

	def EquipementMasque(self):
		if self.MasqueCommunÉquipé == True :
			self.MasqueCommunÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Masque déséquipé")
		else : 
			self.MasqueCommunÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Masque équipé")

	def EquipementTails(self):
		if self.TailsÉpiqueÉquipé == True :
			self.TailsÉpiqueÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Tails déséquipé")
		else : 
			self.TailsÉpiqueÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Tails équipé")

	def EquipementShiba(self):
		if self.ShibaRareÉquipé == True :
			self.ShibaRareÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Shiba déséquipé")
		else : 
			self.ShibaRareÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Shiba équipé")

	def EquipementYeuxRouge(self):
		if self.YeuxRougeRareÉquipé == True :
			self.YeuxRougeRareÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Yeux rouge déséquipé")
		else : 
			self.YeuxRougeRareÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Yeux rouge équipé")

	def EquipementDrip(self):
		if self.LégendaireÉquipé == True :
			self.LégendaireÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Drip déséquipé")
		else : 
			self.LégendaireÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Drip équipé")

	def EquipementNul(self):
		self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Non débloqué")

	def pageCaisse(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.salleTirage = PhotoImage(file="salle/salleTirage.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.salleTirage)

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueDeuxième)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)
		self.boutonCollection = Button(self.EcranDeJeux, text=" Collection ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageCollection)
		self.boutonCollection = self.CanvaUn.create_window(self.LargeurEcran/2+415, 680, window=self.boutonCollection)
		self.boutonDrop = Button(self.EcranDeJeux, text=" Drop ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageDrop)
		self.boutonDrop = self.CanvaUn.create_window(self.LargeurEcran/2-463, 680, window=self.boutonDrop)
		self.boutonTirage = Button(self.EcranDeJeux, text="Tirer une caisse : " + str(self.prixCaisse) +"€", font=("OCR A Extended", 20), bg='white', fg='black', command=self.debitArgentCaisse)
		self.boutonTirage = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2, window=self.boutonTirage)

		### Textes ###
		self.texteChanceLégendaire = self.CanvaUn.create_text(self.LargeurEcran/2, 120, text= "Légendaire - 1%", font=("OCR A Extended", 30), fill="yellow")
		self.texteChanceÉpique = self.CanvaUn.create_text(self.LargeurEcran/2, 170, text= "Épique - 9%", font=("OCR A Extended", 30), fill="purple")
		self.texteChanceRare = self.CanvaUn.create_text(self.LargeurEcran/2, 220, text= "Rare - 35%", font=("OCR A Extended", 30), fill="aqua")
		self.texteChanceCommun = self.CanvaUn.create_text(self.LargeurEcran/2, 270, text= "Commun - 55%", font=("OCR A Extended", 30), fill="grey")
		self.résultatDuTiragePrécédent = self.CanvaUn.create_text(self.LargeurEcran/2-300, self.HauteurEcran/2+100, text= "", font=("OCR A Extended", 15), fill="#FF14E6")
		self.résultatDuTirageActuel = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2+100, text= "", font=("OCR A Extended", 25), fill="#FF14E6")
		self.résultatDuTirageSuivant = self.CanvaUn.create_text(self.LargeurEcran/2+300, self.HauteurEcran/2+100, text= "", font=("OCR A Extended", 15), fill="#FF14E6")
		self.résultatDuTirageFinale = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2+175, text= "", font=("OCR A Extended", 15), fill="#FF14E6")
		self.ArgentTextuel()

	def pageDrop(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.salleDrop = PhotoImage(file="salle/salleDrop.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.salleDrop)

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageCaisse)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		self.dropLunette = self.CanvaUn.create_text((self.LargeurEcran/2+3), 153, text= "Lunette : 10%", font=("OCR A Extended", 30), fill="white")
		self.dropLunetteD = self.CanvaUn.create_text((self.LargeurEcran/2), 150, text= "Lunette : 10%", font=("OCR A Extended", 30), fill="grey")
		self.dropCasquette = self.CanvaUn.create_text((self.LargeurEcran/2+3), 203, text= "Casquette : 17%", font=("OCR A Extended", 30), fill="white")
		self.dropCasquetteD = self.CanvaUn.create_text((self.LargeurEcran/2), 200, text= "Casquette : 17%", font=("OCR A Extended", 30), fill="grey")
		self.dropBoucleOreille = self.CanvaUn.create_text((self.LargeurEcran/2+3), 253, text= "Boucle d'oreilles : 15%", font=("OCR A Extended", 30), fill="white")
		self.dropBoucleOreille = self.CanvaUn.create_text((self.LargeurEcran/2), 250, text= "Boucle d'oreilles : 15%", font=("OCR A Extended", 30), fill="grey")
		self.dropMasque = self.CanvaUn.create_text((self.LargeurEcran/2+3), 303, text= "Masque : 13%", font=("OCR A Extended", 30), fill="white")
		self.dropMasqueD = self.CanvaUn.create_text((self.LargeurEcran/2), 300, text= "Masque : 13%", font=("OCR A Extended", 30), fill="grey")
		self.dropYeuxRouge = self.CanvaUn.create_text((self.LargeurEcran/2+3), 353, text= "Yeux rouge : 21%", font=("OCR A Extended", 30), fill="white")
		self.dropYeuxRougeD = self.CanvaUn.create_text((self.LargeurEcran/2), 350, text= "Yeux rouge : 21%", font=("OCR A Extended", 30), fill="aqua")
		self.dropShiba = self.CanvaUn.create_text((self.LargeurEcran/2+3), 403, text= "Shiba : 14%", font=("OCR A Extended", 30), fill="white")
		self.dropShibaD = self.CanvaUn.create_text((self.LargeurEcran/2), 400, text= "Shiba : 14%", font=("OCR A Extended", 30), fill="aqua")
		self.dropTail = self.CanvaUn.create_text((self.LargeurEcran/2+3), 453, text= "Tail : 9%", font=("OCR A Extended", 30), fill="white")
		self.dropTail = self.CanvaUn.create_text((self.LargeurEcran/2), 450, text= "Tail : 9%", font=("OCR A Extended", 30), fill="purple")
		self.dropLégendaire = self.CanvaUn.create_text((self.LargeurEcran/2+3), 503, text= "Légendaire : 1%", font=("OCR A Extended", 30), fill="white")
		self.dropLégendaire = self.CanvaUn.create_text((self.LargeurEcran/2), 500, text= "Légendaire : 1%", font=("OCR A Extended", 30), fill="yellow")

	def tirageCaisse(self):
		self.CanvaUn.delete(self.boutonTirage)
		self.CanvaUn.delete(self.boutonRetour)
		self.CanvaUn.delete(self.boutonCollection)
		self.CanvaUn.itemconfigure(self.résultatDuTirageFinale, text="")
		while self.compteur < 30 :
			self.calculCaisse()
			time.sleep(0.1)
			self.CanvaUn.update()
		self.compteur = 0
		while self.compteur < 7 :
			self.calculCaisse()
			time.sleep(0.7)
			self.CanvaUn.update()
		self.compteur = 0
		while self.compteur < 3 :
			self.calculCaisse()
			time.sleep(1.5)
			self.CanvaUn.update()
		self.CanvaUn.itemconfigure(self.résultatDuTirageFinale, text=("Vous avez remporté un cosmétique : " + self.résultatActuelString), fill=self.couleurRésultatActuel)
		self.boutonTirage = Button(self.EcranDeJeux, text="Tirer une caisse : " + str(self.prixCaisse) +"€", font=("OCR A Extended", 20), bg='white', fg='black', command=self.debitArgentCaisse)
		self.boutonTirage = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2, window=self.boutonTirage)
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)
		self.boutonCollection = Button(self.EcranDeJeux, text=" Collection ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageCollection)
		self.boutonCollection = self.CanvaUn.create_window(self.LargeurEcran/2+415, 680, window=self.boutonCollection)
		if self.résultatActuelString == "Lunette" :
			self.LunetteCommunPossession = True
		elif self.résultatActuelString == "Casquette" :
			self.CasquetteCommunPossession = True
		elif self.résultatActuelString == "Boucle d'oreilles" :
			self.BoucleOreilleCommunPossession = True
		elif self.résultatActuelString == "Masque" :
			self.MasqueCommunPossession = True
		elif self.résultatActuelString == "Yeux rouge" :
			self.YeuxRougeRarePossession = True
		elif self.résultatActuelString == "Shiba" :
			self.ShibaRarePossession = True
		elif self.résultatActuelString == "Tail" :
			self.TailsÉpiquePossession = True
		elif self.résultatActuelString == "Légendaire" :
			self.LégendairePossession = True
		else :
			None

	def debitArgentCaisse(self):
		if self.argent >= self.prixCaisse :
			self.argent = self.argent - self.prixCaisse
			self.prixCaisse = self.prixCaisse * 2
			self.ActualisationArgent()
			self.tirageCaisse()
		else :
			None	

	def calculCaisse(self):
		couleurRésultatPrécédent = "grey"
		couleurRésultatSuivant = "grey"
		résultatPrécédentString = self.contenuCaisse[self.résultatPrécédent]
		self.résultatActuelString = self.contenuCaisse[self.résultatActuel]
		résulatSuivantString = self.contenuCaisse[self.résulatSuivant]
		### Résultat Précédent ###
		if résultatPrécédentString == "Lunette" or résultatPrécédentString == "Casquette" or résultatPrécédentString == "Boucle d'oreilles" or résultatPrécédentString == "Masque" :
			couleurRésultatPrécédent = "grey"
		elif résultatPrécédentString == "Yeux rouge" or résultatPrécédentString =="Shiba" :
			couleurRésultatPrécédent = "aqua"
		elif résultatPrécédentString == "Tail" :
			couleurRésultatPrécédent = "purple"
		else :
			couleurRésultatPrécédent = "yellow"
		### Résultat Actuel ###
		if self.résultatActuelString == "Lunette" or self.résultatActuelString == "Casquette" or  self.résultatActuelString == "Boucle d'oreilles" or self.résultatActuelString == "Masque" :
			self.couleurRésultatActuel = "grey"
		elif self.résultatActuelString == "Yeux rouge" or self.résultatActuelString == "Shiba" :
			self.couleurRésultatActuel = "aqua"
		elif self.résultatActuelString == "Tail" :
			self.couleurRésultatActuel = "purple"
		else :
			self.couleurRésultatActuel = "yellow"
		### Résultat Suivant ###
		if résulatSuivantString == "Lunette" or résulatSuivantString == "Casquette" or résulatSuivantString == "Boucle d'oreilles" or résulatSuivantString == "Masque" :
			couleurRésultatSuivant = "grey"
		elif résulatSuivantString == "Yeux rouge" or résulatSuivantString =="Shiba" :
			couleurRésultatSuivant = "aqua"
		elif résulatSuivantString == "Tail" :
			couleurRésultatSuivant = "purple"
		else :
			couleurRésultatSuivant = "yellow"
		self.CanvaUn.itemconfigure(self.résultatDuTiragePrécédent, text=résultatPrécédentString, fill=couleurRésultatPrécédent)
		self.CanvaUn.itemconfigure(self.résultatDuTirageActuel, text=self.résultatActuelString, fill=self.couleurRésultatActuel)
		self.CanvaUn.itemconfigure(self.résultatDuTirageSuivant, text=résulatSuivantString, fill=couleurRésultatSuivant)
		self.résultatPrécédent = self.résultatActuel
		self.résultatActuel = self.résulatSuivant
		self.résulatSuivant = random.randint(0, 99)
		self.compteur = self.compteur + 1

	def pageWaifu(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/pageWaifu.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Autres ###
		self.pageWaifuUn()

	def pageWaifuUn(self):
		### Reset ###
		self.CanvaUn.delete(self.affichageArgent)
		self.CanvaUn.delete(self.affichageArgentDouble)
		self.CanvaUn.delete(self.affichageArgentTriple)

		### Images ###
		self.imageWaifuUnNoir = PhotoImage(file="salle/waifuUnPetitNoir.png")
		self.imageWaifuUnColor = PhotoImage(file="salle/waifuUnPetitColor.png")

		### Boutons ###
		if self.waifuUn == False :
			self.boutonWaifuUn = Button(self.EcranDeJeux, image=self.imageWaifuUnNoir, command=self.AchatLyne, borderwidth=0)
			self.boutonWaifuUn = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonWaifuUn)
		else :
			self.boutonWaifuUn = Button(self.EcranDeJeux, image=self.imageWaifuUnColor, command=None, borderwidth=0)
			self.boutonWaifuUn = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonWaifuUn)
		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageWaifuUn)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageWaifuUn)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)

		### Textes ###
		self.texteNomWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+233, (self.HauteurEcran/2)-200, text= "Lyne", font=("OCR A Extended", 30), fill="white")
		self.texteNomWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+230, (self.HauteurEcran/2)-203, text= "Lyne", font=("OCR A Extended", 30), fill="black")
		self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+223, (self.HauteurEcran/2)-103, text= "Augmentera la puissance\n     de vos cliques", font=("OCR A Extended", 30), fill="white")
		self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+220, (self.HauteurEcran/2)-100, text= "Augmentera la puissance\n     de vos cliques", font=("OCR A Extended", 30), fill="black")
		if self.waifuUn == False :
			self.prixWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+233, (self.HauteurEcran/2)+203, text= "Prix : 5.000 €", font=("OCR A Extended", 30), fill="white")
			self.prixWaifuDouuble = self.CanvaUn.create_text((self.LargeurEcran/2)+230, (self.HauteurEcran/2)+200, text= "Prix : 5.000 €", font=("OCR A Extended", 30), fill="black")
		self.ArgentTextuel()

	def AchatLyne(self):
		if self.argent >= 5000 :
			self.CanvaUn.delete(self.affichageArgent)
			self.CanvaUn.delete(self.affichageArgentDouble)
			self.CanvaUn.delete(self.affichageArgentTriple)
			self.argent = self.argent - 5000
			self.waifuUn = True
			self.nombreWaifu = self.nombreWaifu + 1
			self.puissanceClique = 2
			self.ActualisationArgent()
			self.pageWaifuUn()

	def Ressources(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/shop.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)
		self.boutonAchatWeebs = Button(self.EcranDeJeux, text=" Achat weeb (1€/5 Seconde) pour 10€ ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.AchatWeebUn)
		self.boutonAchatWeebs = self.CanvaUn.create_window(self.LargeurEcran/2, 300, window=self.boutonAchatWeebs)
		self.boutonFoisUn = Button(self.EcranDeJeux, text="x1", font=("OCR A Extended", 20), bg='white', fg='black', command=self.RessourcesFois10)
		self.boutonFoisUn = self.CanvaUn.create_window(self.LargeurEcran/2, 200, window=self.boutonFoisUn)

		### Texte ###
		self.ArgentTextuel()

	def RessourcesFois10(self):
		### Reset ###
		self.CanvaUn.delete(self.boutonFoisUn)
		self.CanvaUn.delete(self.boutonAchatWeebs)

		### Boutons ###
		self.boutonAchatWeebs = Button(self.EcranDeJeux, text=" Achat weeb (10€/5 Seconde) pour 100€ ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.AchatWeebDix)
		self.boutonAchatWeebs = self.CanvaUn.create_window(self.LargeurEcran/2, 300, window=self.boutonAchatWeebs)
		self.boutonFoisUn = Button(self.EcranDeJeux, text="x10", font=("OCR A Extended", 20), bg='white', fg='black', command=self.RessourcesFois100)
		self.boutonFoisUn = self.CanvaUn.create_window(self.LargeurEcran/2, 200, window=self.boutonFoisUn)

	def RessourcesFois100(self):
		### Reset ###
		self.CanvaUn.delete(self.boutonFoisUn)
		self.CanvaUn.delete(self.boutonAchatWeebs)

		### Boutons ###
		self.boutonAchatWeebs = Button(self.EcranDeJeux, text=" Achat weeb (100€/5 Seconde) pour 1000€ ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.AchatWeebCent)
		self.boutonAchatWeebs = self.CanvaUn.create_window(self.LargeurEcran/2, 300, window=self.boutonAchatWeebs)
		self.boutonFoisUn = Button(self.EcranDeJeux, text="x100", font=("OCR A Extended", 20), bg='white', fg='black', command=self.RessourcesFois1000)
		self.boutonFoisUn = self.CanvaUn.create_window(self.LargeurEcran/2, 200, window=self.boutonFoisUn)

	def RessourcesFois1000(self):
		### Reset ###
		self.CanvaUn.delete(self.boutonFoisUn)
		self.CanvaUn.delete(self.boutonAchatWeebs)

		### Boutons ###
		self.boutonAchatWeebs = Button(self.EcranDeJeux, text=" Achat weeb (1000€/5 Seconde) pour 10000€ ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.AchatWeebMille)
		self.boutonAchatWeebs = self.CanvaUn.create_window(self.LargeurEcran/2, 300, window=self.boutonAchatWeebs)
		self.boutonFoisUn = Button(self.EcranDeJeux, text="x1000", font=("OCR A Extended", 20), bg='white', fg='black', command=self.Ressources)
		self.boutonFoisUn = self.CanvaUn.create_window(self.LargeurEcran/2, 200, window=self.boutonFoisUn)

	def AchatWeebUn(self):
		if self.argent >= 10 :
			self.argent = self.argent - 10
			self.weeb = self.weeb + 1
			self.ActualisationArgent()
	def AchatWeebDix(self):
		if self.argent >= 100 :
			self.argent = self.argent - 100
			self.weeb = self.weeb + 10
			self.ActualisationArgent()
	def AchatWeebCent(self):
		if self.argent >= 1000 :
			self.argent = self.argent - 1000
			self.weeb = self.weeb + 100
			self.ActualisationArgent()
	def AchatWeebMille(self):
		if self.argent >= 10000 :
			self.argent = self.argent - 10000
			self.weeb = self.weeb + 1000
			self.ActualisationArgent()

	def ActualisationArgent(self):
		self.CanvaUn.itemconfigure(self.affichageArgent, text=self.argent)
		self.CanvaUn.itemconfigure(self.affichageArgentDouble, text=self.argent)
		self.CanvaUn.itemconfigure(self.affichageArgentTriple, text=self.argent)

	def ArgentTextuel(self):
		self.affichageArgent = self.CanvaUn.create_text((self.LargeurEcran/2)+6, 76, text= self.argent, font=("OCR A Extended", 30), fill="#1CF8FF")
		self.affichageArgentDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 73, text= self.argent, font=("OCR A Extended", 30), fill="#FF14E6")
		self.affichageArgentTriple = self.CanvaUn.create_text(self.LargeurEcran/2, 70, text= self.argent, font=("OCR A Extended", 30), fill="#FBFF0F")

	def FonctionTimer(self):
		self.argent = self.argent + self.weeb
		self.argentTotal = self.argentTotal + self.weeb
		### Textes ###
		if self.InGame == True :
			self.ActualisationArgent()
		self.CanvaUn.after(5000, self.FonctionTimer)

	def LancerTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="Mio Akiyama/bandeau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, (self.HauteurEcran/2)+245, image=self.bandeau)

		### Textes ###
		self.nomTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)-480, (self.HauteurEcran/2)+160, text= "???", font=("OCR A Extended", 30), fill="white")
		self.premierTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+250, text= "Saaaaaalut !", font=("OCR A Extended", 30), fill="white")

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.PremièrePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+460, (self.HauteurEcran/2)+320, window=self.boutonSuivant)

	def PremièrePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.persoUn = PhotoImage(file="Mio Akiyama/persoUn.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)-150, (self.HauteurEcran/2)-100, image=self.persoUn)
		self.bandeau = PhotoImage(file="Mio Akiyama/bandeau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, (self.HauteurEcran/2)+245, image=self.bandeau)

		### Textes ###
		self.nomTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)-480, (self.HauteurEcran/2)+160, text= "???", font=("OCR A Extended", 30), fill="white")
		self.premierTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+250, text= "Eh oh ! Je suis ici.", font=("OCR A Extended", 30), fill="white")

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.DeuxièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+460, (self.HauteurEcran/2)+320, window=self.boutonSuivant)

	def DeuxièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.persoUn = PhotoImage(file="Mio Akiyama/persoDeux.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)-150, (self.HauteurEcran/2)-100, image=self.persoUn)
		self.bandeau = PhotoImage(file="Mio Akiyama/bandeau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, (self.HauteurEcran/2)+245, image=self.bandeau)

		### Textes ###
		self.nomTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)-480, (self.HauteurEcran/2)+160, text= "???", font=("OCR A Extended", 30), fill="white")
		self.premierTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+200, text= "Ah enfin !", font=("OCR A Extended", 30), fill="white")
		self.deuxièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+250, text= "Je suis votre nouvelle assistante", font=("OCR A Extended", 30), fill="white")
		self.troisièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+300, text= "Mio Akiyama", font=("OCR A Extended", 30), fill="white")

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.TroisèmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+460, (self.HauteurEcran/2)+320, window=self.boutonSuivant)

	def TroisèmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.persoUn = PhotoImage(file="Mio Akiyama/persoTrois.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)+50, (self.HauteurEcran/2)+100, image=self.persoUn)
		self.bandeau = PhotoImage(file="Mio Akiyama/bandeau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, (self.HauteurEcran/2)+245, image=self.bandeau)

		### Textes ###
		self.nomTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)-400, (self.HauteurEcran/2)+160, text= "Mio Akiyama", font=("OCR A Extended", 30), fill="white")
		self.premierTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+230, text= "Bon, commençons !", font=("OCR A Extended", 30), fill="white")
		self.deuxièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+280, text= "Nous avons beaucoup à faire.", font=("OCR A Extended", 30), fill="white")

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.QuatrièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+460, (self.HauteurEcran/2)+320, window=self.boutonSuivant)

	def QuatrièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)
		self.FenetrePrincipale()
		self.CanvaUn.delete(self.boutonQuête)
		self.CanvaUn.delete(self.boutonStats)
		self.CanvaUn.delete(self.boutonArgent)
		self.CanvaUn.delete(self.boutonMenuSauvegarde)
		self.CanvaUn.delete(self.boutonBoutique)
		self.CanvaUn.delete(self.boutonQuitter)

		### Images ###
		self.CanvaUn.delete(self.personnagePrincipale)
		self.bandeau = PhotoImage(file="Mio Akiyama/bandeau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, (self.HauteurEcran/2)-245, image=self.bandeau)
		self.personnagePrincipale = PhotoImage(file="Mio Akiyama/waifuPersonnage.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.personnagePrincipale)

		### Textes ###
		self.nomTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)-420, (self.HauteurEcran/2)-160, text= "Mio Akiyama", font=("OCR A Extended", 20), fill="white")
		self.premierTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-260, text= "J'espère que notre entreprise", font=("OCR A Extended", 25), fill="white")
		self.deuxièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-210, text= "marchera bien ♥.", font=("OCR A Extended", 30), fill="white")

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.CinquièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2), (self.HauteurEcran/2)-100, window=self.boutonSuivant)
		
	def CinquièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)
		self.FenetrePrincipale()
		self.CanvaUn.delete(self.personnagePrincipale)
		self.CanvaUn.delete(self.boutonQuête)
		self.CanvaUn.delete(self.boutonStats)
		self.CanvaUn.delete(self.boutonArgent)
		self.CanvaUn.delete(self.boutonMenuSauvegarde)
		self.CanvaUn.delete(self.boutonBoutique)
		self.CanvaUn.delete(self.boutonQuitter)

		### Images ###
		self.bandeau = PhotoImage(file="Mio Akiyama/bandeau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, (self.HauteurEcran/2)-245, image=self.bandeau)
		self.personnagePrincipale = PhotoImage(file="Mio Akiyama/waifuPersonnage.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.personnagePrincipale)

		### Textes ###
		self.nomTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)-420, (self.HauteurEcran/2)-160, text= "Mio Akiyama", font=("OCR A Extended", 20), fill="white")
		self.premierTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-250, text= "Alors déja, notre source de revenu.", font=("OCR A Extended", 23), fill="white")

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.SixièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2), (self.HauteurEcran/2)-100, window=self.boutonSuivant)
		
	def SixièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)
		self.FenetrePrincipale()
		self.CanvaUn.delete(self.personnagePrincipale)
		self.CanvaUn.delete(self.boutonStats)
		self.CanvaUn.delete(self.boutonArgent)
		self.CanvaUn.delete(self.boutonMenuSauvegarde)
		self.CanvaUn.delete(self.boutonBoutique)
		self.CanvaUn.delete(self.boutonQuitter)
		self.CanvaUn.delete(self.boutonQuête)

		### Images ###
		self.bandeau = PhotoImage(file="Mio Akiyama/bandeau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, (self.HauteurEcran/2)-245, image=self.bandeau)
		self.personnagePrincipale = PhotoImage(file="Mio Akiyama/persoQuatre.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+80, image=self.personnagePrincipale)

		### Textes ###
		self.nomTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)-420, (self.HauteurEcran/2)-160, text= "Mio Akiyama", font=("OCR A Extended", 20), fill="white")
		self.premierTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-300, text= "Allons devenir riche eheh !", font=("OCR A Extended", 25), fill="white")
		self.deuxièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-250, text= "Euh... Pardon patron,", font=("OCR A Extended", 30), fill="white")
		self.troisièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-200, text= "j'ai du mal à rester sérieuse.", font=("OCR A Extended", 25), fill="white")

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.SeptièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2), (self.HauteurEcran/2)-100, window=self.boutonSuivant)
		
	def SeptièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)
		self.FenetrePrincipale()
		self.CanvaUn.delete(self.boutonStats)
		self.CanvaUn.delete(self.boutonArgent)
		self.CanvaUn.delete(self.boutonMenuSauvegarde)
		self.CanvaUn.delete(self.boutonBoutique)
		self.CanvaUn.delete(self.boutonQuitter)
		self.CanvaUn.delete(self.boutonQuête)

		### Images ###
		self.CanvaUn.delete(self.personnagePrincipale)
		self.bandeau = PhotoImage(file="Mio Akiyama/bandeau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, (self.HauteurEcran/2)-245, image=self.bandeau)
		self.personnagePrincipale = PhotoImage(file="Mio Akiyama/waifuPersonnage.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.personnagePrincipale)

		### Textes ###
		self.nomTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)-420, (self.HauteurEcran/2)-160, text= "Mio Akiyama", font=("OCR A Extended", 20), fill="white")
		self.premierTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-300, text= "Alors si vous cliquez içi,", font=("OCR A Extended", 25), fill="white")
		self.deuxièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-250, text= "Vous gagnez 1€ ! C'est pas grand chose", font=("OCR A Extended", 20), fill="white")
		self.troisièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-200, text= "mais ça sera mieux plus tard !", font=("OCR A Extended", 25), fill="white")

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.HuitièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2), (self.HauteurEcran/2)-100, window=self.boutonSuivant)
		self.boutonArgent = Button(self.EcranDeJeux, text=" Vendre des photos ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.SeptièmePageTutoBis)
		self.boutonArgent = self.CanvaUn.create_window(self.LargeurEcran/2, 660, window=self.boutonArgent)

	def SeptièmePageTutoBis(self):
		self.CanvaUn.delete(self.personnagePrincipale)
		self.personnagePrincipale = PhotoImage(file="Mio Akiyama/persoUn.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+100, image=self.personnagePrincipale)

		### Textes ###
		self.CanvaUn.itemconfigure(self.premierTexteTuto, text="Eh...")
		self.CanvaUn.itemconfigure(self.deuxièmeTexteTuto, text="Tu joueras à la fin du tuto.")
		self.CanvaUn.delete(self.troisièmeTexteTuto)

		### Boutons ###
		self.CanvaUn.delete(self.boutonSuivant)
		self.CanvaUn.delete(self.boutonArgent)
		self.boutonSuivant = Button(self.EcranDeJeux, text="Désolé", font=("OCR A Extended", 20), bg='white', fg='black', command=self.TransitionTutoBis)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+470, (self.HauteurEcran/2)+320, window=self.boutonSuivant)

	def TransitionTutoBis(self):
		self.CanvaUn.delete(self.personnagePrincipale)
		self.personnagePrincipale = PhotoImage(file="Mio Akiyama/waifuPersonnage.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.personnagePrincipale)

		### Textes ###
		self.CanvaUn.delete(self.premierTexteTuto)
		self.CanvaUn.itemconfigure(self.deuxièmeTexteTuto, text="Donc,")
		self.CanvaUn.delete(self.troisièmeTexteTuto)

		### Boutons ###
		self.CanvaUn.delete(self.boutonSuivant)
		self.CanvaUn.delete(self.boutonArgent)
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.HuitièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+450, (self.HauteurEcran/2)+320, window=self.boutonSuivant)

	def HuitièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)
		self.FenetrePrincipale()
		self.CanvaUn.delete(self.boutonQuête)
		self.CanvaUn.delete(self.boutonStats)
		self.CanvaUn.delete(self.boutonArgent)
		self.CanvaUn.delete(self.boutonMenuSauvegarde)
		self.CanvaUn.delete(self.boutonBoutique)
		self.CanvaUn.delete(self.boutonQuitter)

		### Images ###
		self.CanvaUn.delete(self.personnagePrincipale)
		self.bandeau = PhotoImage(file="Mio Akiyama/bandeau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, (self.HauteurEcran/2)-245, image=self.bandeau)
		self.personnagePrincipale = PhotoImage(file="Mio Akiyama/waifuPersonnage.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.personnagePrincipale)

		### Textes ###
		self.nomTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)-420, (self.HauteurEcran/2)-160, text= "Mio Akiyama", font=("OCR A Extended", 20), fill="white")
		self.premierTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-270, text= "Les autres boutons sont assez", font=("OCR A Extended", 25), fill="white")
		self.deuxièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-220, text= "évident donc eheh bonne chance !", font=("OCR A Extended", 20), fill="white")
		self.troisièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-170, text= "Tu es assez grand pour comprendre ♥", font=("OCR A Extended", 20), fill="white")
		
		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.NeuvièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2), (self.HauteurEcran/2)-100, window=self.boutonSuivant)
		self.boutonStats = Button(self.EcranDeJeux, text=" Stats ", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonStats = self.CanvaUn.create_window(970, 590, window=self.boutonStats)
		self.boutonArgent = Button(self.EcranDeJeux, text=" Vendre des photos ", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonArgent = self.CanvaUn.create_window(self.LargeurEcran/2, 660, window=self.boutonArgent)
		self.boutonMenuSauvegarde = Button(self.EcranDeJeux, text=" Menu Sauvegarde ", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonMenuSauvegarde = self.CanvaUn.create_window(200, 660, window=self.boutonMenuSauvegarde)
		self.boutonBoutique = Button(self.EcranDeJeux, text=" Boutique ", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonBoutique = self.CanvaUn.create_window(820, 660, window=self.boutonBoutique) 
		self.boutonQuitter = Button(self.EcranDeJeux, text=" ❌ ", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonQuitter = self.CanvaUn.create_window(990, 660, window=self.boutonQuitter)
	
	def NeuvièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)
		self.FenetrePrincipale()
		self.CanvaUn.delete(self.boutonStats)
		self.CanvaUn.delete(self.boutonArgent)
		self.CanvaUn.delete(self.boutonMenuSauvegarde)
		self.CanvaUn.delete(self.boutonBoutique)
		self.CanvaUn.delete(self.boutonQuitter)

		### Images ###
		self.CanvaUn.delete(self.personnagePrincipale)
		self.bandeau = PhotoImage(file="Mio Akiyama/bandeau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, (self.HauteurEcran/2)-245, image=self.bandeau)
		self.personnagePrincipale = PhotoImage(file="Mio Akiyama/waifuPersonnage.png")
		self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.personnagePrincipale)

		### Textes ###
		self.nomTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)-420, (self.HauteurEcran/2)-160, text= "Mio Akiyama", font=("OCR A Extended", 20), fill="white")
		self.premierTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-300, text= "Je vais rester ici pour vous assiter.", font=("OCR A Extended", 20), fill="white")
		self.deuxièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-250, text= "Toute vos tâches à réaliser ce trouve", font=("OCR A Extended", 20), fill="white")
		self.troisièmeTexteTuto = self.CanvaUn.create_text((self.LargeurEcran/2)+200, (self.HauteurEcran/2)-200, text= 'dans le bouton "Quête", je compte sur vous !', font=("OCR A Extended", 18), fill="white")
		
		### Boutons ###
		self.boutonQuête = Button(self.EcranDeJeux, text="Quête", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonQuête = self.CanvaUn.create_window(835, 590, window=self.boutonQuête)
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2), (self.HauteurEcran/2)-100, window=self.boutonSuivant)
		self.boutonStats = Button(self.EcranDeJeux, text=" Stats ", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonStats = self.CanvaUn.create_window(970, 590, window=self.boutonStats)
		self.boutonArgent = Button(self.EcranDeJeux, text=" Vendre des photos ", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonArgent = self.CanvaUn.create_window(self.LargeurEcran/2, 660, window=self.boutonArgent)
		self.boutonMenuSauvegarde = Button(self.EcranDeJeux, text=" Menu Sauvegarde ", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonMenuSauvegarde = self.CanvaUn.create_window(200, 660, window=self.boutonMenuSauvegarde)
		self.boutonBoutique = Button(self.EcranDeJeux, text=" Boutique ", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonBoutique = self.CanvaUn.create_window(820, 660, window=self.boutonBoutique) 
		self.boutonQuitter = Button(self.EcranDeJeux, text=" ❌ ", font=("OCR A Extended", 20), bg='white', fg='black', command=None)
		self.boutonQuitter = self.CanvaUn.create_window(990, 660, window=self.boutonQuitter)

jeux = Jeux()
jeux 