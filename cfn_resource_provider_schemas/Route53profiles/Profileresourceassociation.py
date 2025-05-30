SCHEMA = {
  "typeName" : "AWS::Route53Profiles::ProfileResourceAssociation",
  "description" : "Resource Type definition for AWS::Route53Profiles::ProfileResourceAssociation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-route53profiles",
  "additionalProperties" : False,
  "properties" : {
    "ProfileId" : {
      "description" : "The ID of the  profile that you associated the resource to that is specified by ResourceArn.",
      "type" : "string"
    },
    "Id" : {
      "description" : "Primary Identifier for  Profile Resource Association",
      "type" : "string"
    },
    "Name" : {
      "description" : "The name of an association between the  Profile and resource.",
      "type" : "string"
    },
    "ResourceArn" : {
      "description" : "The arn of the resource that you associated to the  Profile.",
      "type" : "string"
    },
    "ResourceProperties" : {
      "description" : "A JSON-formatted string with key-value pairs specifying the properties of the associated resource.",
      "type" : "string"
    },
    "ResourceType" : {
      "description" : "The type of the resource associated to the  Profile.",
      "type" : "string"
    }
  },
  "required" : [ "ProfileId", "Name", "ResourceArn" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/ResourceType" ],
  "createOnlyProperties" : [ "/properties/ProfileId", "/properties/Name", "/properties/ResourceArn" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "route53profiles:AssociateResourceToProfile", "route53profiles:GetProfileResourceAssociation", "route53resolver:GetFirewallRuleGroup", "route53resolver:GetResolverRule", "route53:GetHostedZone", "route53resolver:GetResolverQueryLogConfig", "ec2:DescribeVpcEndpoints" ]
    },
    "read" : {
      "permissions" : [ "route53profiles:GetProfileResourceAssociation" ]
    },
    "delete" : {
      "permissions" : [ "route53profiles:DisassociateResourceFromProfile", "route53profiles:GetProfileResourceAssociation", "route53resolver:GetFirewallRuleGroup", "route53resolver:GetResolverRule", "route53:GetHostedZone", "route53resolver:GetResolverQueryLogConfig", "ec2:DescribeVpcEndpoints" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ProfileId" : {
            "$ref" : "resource-schema.json#/properties/ProfileId"
          }
        },
        "required" : [ "ProfileId" ]
      },
      "permissions" : [ "route53profiles:ListProfileResourceAssociations" ]
    },
    "update" : {
      "permissions" : [ "route53profiles:UpdateProfileResourceAssociation" ]
    }
  }
}