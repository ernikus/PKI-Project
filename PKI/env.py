### LIBRARIES #################################################################

import os
import subprocess

############################################################################

# create "tls" folder
directory = "tls"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)


direccerts = "certs"
path1 = os.path.join(path, direccerts)


os.mkdir(path)
os.chdir(path)

# certs -   public certificates
# private - private certtficates
# crf -     revoked certtficates
directory = ['certs', 'private', 'crl']

for directory in directory:
    path2 = os.path.join(path, directory)
    os.mkdir(path2)

file = ['index.txt', 'serial', 'crlnumber', 'openssl.cnf', 'temp.pem', 'ext_template.cnf']

for file in file:
    if file == 'serial':
        f = open(file, "a")
        f.write("01")
        f.close()
    elif file == "crlnumber":
        f = open(file, "a")
        f.write("1000")
        f.close()
    elif file == "ext_template.cnf":
        os.chdir(path1)
        f = open(file, "a")
        f.write("""basicConstraints = CA:FALSE
nsCertType = client, email
nsComment = "OpenSSL Generated Client Certificate"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth, serverAuth""")
        f.close()
    elif file == "openssl.cnf":
        f = open(file, "a")
        f.write("""[ ca ]
default_ca      = CA_default            # The default ca section

[ CA_default ]
dir             = """ + path + """            # Where everything is kept
certs           = $dir/certs            # Where the issued certs are kept
crl_dir         = $dir/crl              # Where the issued crl are kept
database        = $dir/index.txt        # database index file.
new_certs_dir   = $dir/certs            # default place for new certs.
certificate     = $dir/certs/cacert.pem         # The CA certificate
serial          = $dir/serial           # The current serial number
crlnumber       = $dir/crlnumber        # the current crl number
crl             = $dir/crl.pem          # The current CRL
private_key     = $dir/private/cakey.pem # The private key
x509_extensions = v3_ca                 # The extensions to add to the cert
name_opt        = ca_default            # Subject Name options
cert_opt        = ca_default            # Certificate field options

# crlnumber must also be commented out to leave a V1 CRL.
 crl_extensions = crl_ext

default_days    = 365                   # how long to certify for
default_crl_days= 30                    # how long before next CRL
default_md      = sha256                # use SHA-256 by default
preserve        = no                    # keep passed DN ordering

policy          = policy_match

# For the CA policy
[ policy_match ]
countryName             = optional
stateOrProvinceName     = optional
organizationName        = optional
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

####################################################################
[ req ]
default_bits            = 2048
default_md              = sha256
default_keyfile         = privkey.pem
distinguished_name      = req_distinguished_name
attributes              = req_attributes
x509_extensions = v3_ca # The extensions to add to the self signed cert

[ req_distinguished_name ]
countryName                     = Country Name (2 letter code)
countryName_default             = PL
stateOrProvinceName             = State or Province Name (full name)
stateOrProvinceName_default     = DolnoSlaskie
localityName                    = Locality Name (eg, city)
localityName_default            = Wroclaw
0.organizationName              = Organization Name (eg, company)
0.organizationName_default      = PWR
organizationalUnitName          = Organizational Unit Name (eg, section)
organizationalUnitName_default  = Admin

commonName                      = Common Name (eg, your name or your server\'s hostname)
commonName_max                  = 64

emailAddress                    = Email Address
emailAddress_max                = 64

[ req_attributes ]
challengePassword               = A challenge password
challengePassword_min           = 4
challengePassword_max           = 20
unstructuredName                = An optional company name

[ v3_req ]
# Extensions to add to a certificate request
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment

[ v3_ca ]
# Extensions for a typical CA
# PKIX recommendation.
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid:always,issuer
basicConstraints = critical,CA:true

[ crl_ext ]
# CRL extensions.
# Only issuerAltName and authorityKeyIdentifier make any sense in a CRL.
authorityKeyIdentifier=keyid:always""")
        f.close()
    else:
        f = open(file, "a")
        f.close()
