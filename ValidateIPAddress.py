class Solution:
    def validIPAddress(self, IP: str) -> str:
        if ('.' in IP) and (':' in IP): return "Neither"
        if '.' in IP:
            x = IP.split(".")
            if len(x) != 4: return "Neither"
            for i in x:
                if i.isdigit() == False or (i[0] == "0" and int(i) > 0) or int(i) > 255:
                    return "Neither"
                if i[0] == '0' and int(i) == 0 and len(i) > 1:
                    return "Neither"
            return "IPv4"

        elif ':' in IP:
            if "::" in IP: return "Neither"
            x = IP.split(":")
            if len(x) != 8: return "Neither"
            if x[0][0] == '0':
                return "Neither"

            for i in x:
                if len(i) > 4: return "Neither"
                if i.isdigit() == False:
                    for dig in i:
                        if dig.isdigit() == False:
                            if not (dig >= 'a' and dig <= 'z') and not (dig >= 'A' and dig <= 'Z'): return "Neither"
                            if (dig >= 'g' and dig <= 'z') or (dig >= 'G' and dig <= 'Z'):
                                return "Neither"

            return "IPv6"

        return "Neither"