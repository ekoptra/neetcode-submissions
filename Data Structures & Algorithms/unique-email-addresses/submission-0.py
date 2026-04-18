class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        for email in emails:
            local_name, domain = email.split("@")
            local_name = local_name.split("+")[0]
            local_name = "".join([s for s in local_name if s != '.'])
            full_email = f"{local_name}@{domain}"
            if full_email not in s:
                s.add(full_email)
        
        return len(s)
