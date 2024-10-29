from GatariAPI import user_stats

u_id = 1000
mode = 0                    
user = user_stats(u_id, mode)
print(user.pp()) 