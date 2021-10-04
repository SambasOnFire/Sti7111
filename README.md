# Sti7111
Exploit cwpk

This is based on pdf of secure-exploitation. 
http://www.security-explorations.com/

Thank you for this amazing work!

Okey, let's go...

First Set-top-box need have uart port active(TX/RX).

Sometimes engineers make stupid mistakes(lucky for us)

After enter on box must check if this is vulnerable or not.

Type cmd.

peek fe00d05c

If this return 0x00000000(yeah), case not ,sorry this not for you.

Final key is on address fe24c020. 
