SCHEMA = {
  "typeName" : "AWS::Route53Resolver::ResolverDNSSECConfig",
  "description" : "Resource schema for AWS::Route53Resolver::ResolverDNSSECConfig.",
  "properties" : {
    "Id" : {
      "description" : "Id",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "OwnerId" : {
      "description" : "AccountId",
      "type" : "string",
      "minLength" : 12,
      "maxLength" : 32
    },
    "ResourceId" : {
      "description" : "ResourceId",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "ValidationStatus" : {
      "description" : "ResolverDNSSECValidationStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.",
      "type" : "string",
      "enum" : [ "ENABLING", "ENABLED", "DISABLING", "DISABLED" ]
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "readOnlyProperties" : [ "/properties/OwnerId", "/properties/Id", "/properties/ValidationStatus" ],
  "createOnlyProperties" : [ "/properties/ResourceId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "resolverdnssec:CreateConfig", "route53resolver:UpdateResolverDnssecConfig", "route53resolver:GetResolverDnssecConfig", "ec2:DescribeVpcs" ]
    },
    "read" : {
      "permissions" : [ "resolverdnssec:GetConfig", "route53resolver:ListResolverDnssecConfigs" ]
    },
    "delete" : {
      "permissions" : [ "resolverdnssec:DeleteConfig", "route53resolver:UpdateResolverDnssecConfig", "route53resolver:ListResolverDnssecConfigs", "ec2:DescribeVpcs" ]
    },
    "list" : {
      "permissions" : [ "resolverdnssec:ListConfig", "route53resolver:ListResolverDnssecConfigs" ]
    }
  }
}