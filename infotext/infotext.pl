#!/usr/bin/perl
reader();
sub reader(){
	$count=0;
	@new=[];
	print"\t\t** WELCOME TO UPPERCASING TEXT **\n\n";
	print"#--> Enter your text\n";
	print"KALI\@UPPER ~\$ ";
	$text=<STDIN>;
	print"Query 1, OK !\n";
	@new=$text;
	print"this is the length of your text --> ",length($text)-1,"\n";
	print uc(@new[$count]);
}
	
