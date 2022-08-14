def numUniqueEmails(emails):
    new = []
    for i in emails:
        new.append(i.split("@"))
    for j in range(len(new)):
        new[j][0] = new[j][0].replace(".", "").split("+")[0]
        new[j] = "@".join(new[j])
    return(len(set(new)))
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))
