SCHEMA = {
  "typeName" : "AWS::Route53::KeySigningKey",
  "description" : "Represents a key signing key (KSK) associated with a hosted zone. You can only have two KSKs per hosted zone.",
  "properties" : {
    "HostedZoneId" : {
      "description" : "The unique string (ID) used to identify a hosted zone.",
      "type" : "string",
      "pattern" : "^[A-Z0-9]{1,32}$"
    },
    "Status" : {
      "description" : "A string specifying the initial status of the key signing key (KSK). You can set the value to ACTIVE or INACTIVE.",
      "type" : "string",
      "enum" : [ "ACTIVE", "INACTIVE" ]
    },
    "Name" : {
      "description" : "An alphanumeric string used to identify a key signing key (KSK). Name must be unique for each key signing key in the same hosted zone.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_]{3,128}$"
    },
    "KeyManagementServiceArn" : {
      "description" : "The Amazon resource name (ARN) for a customer managed key (CMK) in AWS Key Management Service (KMS). The KeyManagementServiceArn must be unique for each key signing key (KSK) in a single hosted zone.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256
    }
  },
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/HostedZoneId", "/properties/Name", "/properties/KeyManagementServiceArn" ],
  "required" : [ "Status", "HostedZoneId", "Name", "KeyManagementServiceArn" ],
  "primaryIdentifier" : [ "/properties/HostedZoneId", "/properties/Name" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "route53:CreateKeySigningKey", "kms:DescribeKey", "kms:GetPublicKey", "kms:Sign", "kms:CreateGrant" ]
    },
    "read" : {
      "permissions" : [ "route53:GetDNSSEC" ]
    },
    "update" : {
      "permissions" : [ "route53:GetDNSSEC", "route53:ActivateKeySigningKey", "route53:DeactivateKeySigningKey", "kms:DescribeKey", "kms:GetPublicKey", "kms:Sign", "kms:CreateGrant" ]
    },
    "delete" : {
      "permissions" : [ "route53:DeactivateKeySigningKey", "route53:DeleteKeySigningKey", "kms:DescribeKey", "kms:GetPublicKey", "kms:Sign", "kms:CreateGrant" ]
    },
    "list" : {
      "permissions" : [ "route53:GetDNSSEC", "route53:ListHostedZones" ]
    }
  }
}