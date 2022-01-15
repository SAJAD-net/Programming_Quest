require 'open-uri'
require 'nokogiri'

def go()
  puts "- Getting The Complete List of Hacker And Cybersecurity Movies\n"
  
  url = "https://cybersecurityventures.com/movies-about-cybersecurity-and-hacking/"

  html = URI.open(url)
  response = Nokogiri::HTML(html)
  
  count = 0
  ptag = response.css('p')
  
  for thing in ptag
    date = (thing.text).match(/(\d*) —/)
    if date != nil
      name = thing.css('a').text
      puts "#{date}  #{name}\n--------"
      count +=1
    end
  end
  puts "\n- total movies : #{count}" 

end

go()
