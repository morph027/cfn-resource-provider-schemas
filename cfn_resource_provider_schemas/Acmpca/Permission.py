SCHEMA = {
  "typeName" : "AWS::ACMPCA::Permission",
  "description" : "Permission set on private certificate authority",
  "sourceUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ACMPCA.html",
  "properties" : {
    "Actions" : {
      "description" : "The actions that the specified AWS service principal can use. Actions IssueCertificate, GetCertificate and ListPermissions must be provided.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "CertificateAuthorityArn" : {
      "description" : "The Amazon Resource Name (ARN) of the Private Certificate Authority that grants the permission.",
      "type" : "string"
    },
    "Principal" : {
      "description" : "The AWS service or identity that receives the permission. At this time, the only valid principal is acm.amazonaws.com.",
      "type" : "string"
    },
    "SourceAccount" : {
      "description" : "The ID of the calling account.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "Actions", "CertificateAuthorityArn", "Principal" ],
  "createOnlyProperties" : [ "/properties/Actions", "/properties/CertificateAuthorityArn", "/properties/Principal", "/properties/SourceAccount" ],
  "primaryIdentifier" : [ "/properties/CertificateAuthorityArn", "/properties/Principal" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "acm-pca:CreatePermission", "acm-pca:ListPermissions" ]
    },
    "read" : {
      "permissions" : [ "acm-pca:ListPermissions" ]
    },
    "delete" : {
      "permissions" : [ "acm-pca:DeletePermission" ]
    }
  }
}