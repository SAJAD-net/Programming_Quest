#Jcat 

#help function 
function help()
    println("usage : julia jcat.jl [ARGS] [FILE_NAME]")
    println("args  :\n\t-s [time] --> read each line automaticaly with user time wait")
    exit()
end

#Reads the file and displays it's context
function reader()
    #checks the user inputs
    for arg in ARGS
    	if length(arg) > 2
		global fname = arg
    	else
	    help()
    	end
    end

    #Reads the file 	 
    try
    	global fname
    	open(fname) do f
    	    while ! eof(f)
    	        line = readline(f) #Reads the file line by line
	    	if "-s" in ARGS
		    time = parse(Float64,ARGS[2]) #User time input
	   	    sleep(time) #Waits for [time] in second 
		end
		println(line)	
            end
    	end
    catch
	help()
    end
end

reader()

