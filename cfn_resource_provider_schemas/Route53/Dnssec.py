SCHEMA = {
  "typeName" : "AWS::Route53::DNSSEC",
  "description" : "Resource used to control (enable/disable) DNSSEC in a specific hosted zone.",
  "properties" : {
    "HostedZoneId" : {
      "description" : "The unique string (ID) used to identify a hosted zone.",
      "type" : "string",
      "pattern" : "^[A-Z0-9]{1,32}$"
    }
  },
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/HostedZoneId" ],
  "required" : [ "HostedZoneId" ],
  "primaryIdentifier" : [ "/properties/HostedZoneId" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "route53:GetDNSSEC", "route53:EnableHostedZoneDNSSEC", "kms:DescribeKey", "kms:GetPublicKey", "kms:Sign", "kms:CreateGrant" ]
    },
    "read" : {
      "permissions" : [ "route53:GetDNSSEC" ]
    },
    "delete" : {
      "permissions" : [ "route53:GetDNSSEC", "route53:DisableHostedZoneDNSSEC", "kms:DescribeKey", "kms:GetPublicKey", "kms:Sign", "kms:CreateGrant" ]
    },
    "list" : {
      "permissions" : [ "route53:GetDNSSEC", "route53:ListHostedZones" ]
    }
  }
}