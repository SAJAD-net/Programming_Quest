import net.http
import os

fn ipinfo(ip string) ?string {
    url := 'https://ipapi.co/$ip/json/'
    res := http.get(url)?
    return res.text

}

fn myip() ?string {
    url := "http://icanhazip.com"
    res := http.get(url)?
    return res.text 
}

fn help() {
    println("enter valid args !")
    println("iptools ~\n\t-i {ip} ~ displays your ip information \ 
    \n\t-m ~ displays your ip address")
}

fn main() {
    if os.args.len > 1 {
        if os.args[1] == "-i" {
            ip := os.args[2]
            println(ipinfo(ip)?)
        }else if os.args[1] == "-m" { 
            println(myip()?)    
        }else { 
            help()
        }
    }else { 
        help()
    }
}


