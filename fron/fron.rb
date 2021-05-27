

#this is a help function 
def help
	puts """[!]--> dof help :
	[1]- -t --> is a file or dir
	[2]- -n --> num of file and dir in a folder 
	[3]- -h --> show help
	"""
end

#and this is dir or file function (dof)
def dof
	if ARGV.length > 0
		df = ARGV[1]
		puts "[!]--> #{df} --> #{File.ftype(df)}"
	else 
		puts "[!]--> enter name of it !"
	end
end

#well, this is num of file function (nof)
def nof
	if ARGV.length > 0
		if not(File.file?(ARGV[1]))	
			fol = ARGV[1]
			all = Dir.children(fol) 
			na = all.length
			nf, nd = 0, 0
			all.each do |thing|
				if File.file?(thing)
					nf += 1 
				else
					nd += 1
				end
			end
			puts """[!]--> num of any thing in '#{fol}' : 
	[!]--> num of all thing  --> #{na}
	[!]--> num of file  	 --> #{nf}
	[!]--> num of dir  	 --> #{nd}"""
		else
			puts "[!]--> this is not a dir ! #{fol}"
		end
		
	end
end

#it is a run and main function 
def run 
	if ARGV.length > 0
		if ARGV[0] == "-t"
			dof
		elsif ARGV[0] == "-n"
			nof
		elsif ARGV[0] == "-h"
			help
		else
			puts "[!]--> enter valid args !" 
		end
	end
end

run
