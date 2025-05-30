SCHEMA = {
  "typeName" : "AWS::ACMPCA::CertificateAuthorityActivation",
  "description" : "Used to install the certificate authority certificate and update the certificate authority status.",
  "sourceUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ACMPCA.html",
  "properties" : {
    "CertificateAuthorityArn" : {
      "description" : "Arn of the Certificate Authority.",
      "type" : "string"
    },
    "Certificate" : {
      "description" : "Certificate Authority certificate that will be installed in the Certificate Authority.",
      "type" : "string"
    },
    "CertificateChain" : {
      "description" : "Certificate chain for the Certificate Authority certificate.",
      "type" : "string"
    },
    "Status" : {
      "description" : "The status of the Certificate Authority.",
      "type" : "string"
    },
    "CompleteCertificateChain" : {
      "description" : "The complete certificate chain, including the Certificate Authority certificate.",
      "type" : "string"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "CertificateAuthorityArn", "Certificate" ],
  "createOnlyProperties" : [ "/properties/CertificateAuthorityArn" ],
  "writeOnlyProperties" : [ "/properties/Certificate", "/properties/CertificateChain" ],
  "readOnlyProperties" : [ "/properties/CompleteCertificateChain" ],
  "primaryIdentifier" : [ "/properties/CertificateAuthorityArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "acm-pca:ImportCertificateAuthorityCertificate", "acm-pca:UpdateCertificateAuthority" ]
    },
    "read" : {
      "permissions" : [ "acm-pca:GetCertificateAuthorityCertificate", "acm-pca:DescribeCertificateAuthority" ]
    },
    "delete" : {
      "permissions" : [ "acm-pca:UpdateCertificateAuthority" ]
    },
    "update" : {
      "permissions" : [ "acm-pca:ImportCertificateAuthorityCertificate", "acm-pca:UpdateCertificateAuthority" ]
    }
  }
}