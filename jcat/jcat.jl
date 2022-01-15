#Jcat 

#help function 
function help()
    println("usage : julia jcat.jl [ARGS] [FILE_NAME]")
    println("args  :\n\t-s [time] --> read each line automaticaly with user time wait")
    exit()
end

#reader function to read the file and show it's texts
function reader()
    #check the user inputs
    try
	for arg in ARGS
	    if length(arg) > 2 
                global fname = arg
    	    end
	end
    catch
        help()
    end
    #try to read the file 	 
    try
    	global fname
    	open(fname) do f
    	    while ! eof(f)
    	        line = readline(f) #read the file 
	    	if "-s" in ARGS
		    time = parse(Float64,ARGS[2]) #user time input
	   	    sleep(time) #wait for [time] second 
		end
		println(line)	
            end
    	end
	catch
    	    println("can't open this file ~ $fname")
	end
end

reader()

