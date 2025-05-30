SCHEMA = {
  "typeName" : "AWS::DMS::Certificate",
  "description" : "Resource Type definition for AWS::DMS::Certificate",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "CertificateIdentifier" : {
      "type" : "string"
    },
    "CertificatePem" : {
      "type" : "string"
    },
    "CertificateWallet" : {
      "type" : "string"
    }
  },
  "createOnlyProperties" : [ "/properties/CertificateIdentifier", "/properties/CertificatePem", "/properties/CertificateWallet" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}