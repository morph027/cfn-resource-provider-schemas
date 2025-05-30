SCHEMA = {
  "typeName" : "AWS::Route53Resolver::FirewallRuleGroupAssociation",
  "description" : "Resource schema for AWS::Route53Resolver::FirewallRuleGroupAssociation.",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 127
        },
        "Value" : {
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 255
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Id" : {
      "description" : "Id",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "Arn" : {
      "description" : "Arn",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 600
    },
    "FirewallRuleGroupId" : {
      "description" : "FirewallRuleGroupId",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "VpcId" : {
      "description" : "VpcId",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "Name" : {
      "description" : "FirewallRuleGroupAssociationName",
      "type" : "string",
      "pattern" : "(?!^[0-9]+$)([a-zA-Z0-9\\-_' ']+)",
      "minLength" : 0,
      "maxLength" : 64
    },
    "Priority" : {
      "description" : "Priority",
      "type" : "integer"
    },
    "MutationProtection" : {
      "description" : "MutationProtectionStatus",
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "ManagedOwnerName" : {
      "description" : "ServicePrincipal",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 512
    },
    "Status" : {
      "description" : "ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.",
      "type" : "string",
      "enum" : [ "COMPLETE", "DELETING", "UPDATING", "INACTIVE_OWNER_ACCOUNT_CLOSED" ]
    },
    "StatusMessage" : {
      "description" : "FirewallDomainListAssociationStatus",
      "type" : "string"
    },
    "CreatorRequestId" : {
      "description" : "The id of the creator request.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "CreationTime" : {
      "description" : "Rfc3339TimeString",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 40
    },
    "ModificationTime" : {
      "description" : "Rfc3339TimeString",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 40
    },
    "Tags" : {
      "description" : "Tags",
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "route53resolver:TagResource", "route53resolver:UntagResource" ]
  },
  "required" : [ "FirewallRuleGroupId", "VpcId", "Priority" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/FirewallRuleGroupId", "/properties/VpcId" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn", "/properties/ManagedOwnerName", "/properties/Status", "/properties/StatusMessage", "/properties/CreatorRequestId", "/properties/CreationTime", "/properties/ModificationTime" ],
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "route53resolver:AssociateFirewallRuleGroup", "route53resolver:GetFirewallRuleGroupAssociation", "route53resolver:TagResource", "route53resolver:ListTagsForResource", "ec2:DescribeVpcs" ]
    },
    "read" : {
      "permissions" : [ "route53resolver:GetFirewallRuleGroupAssociation", "route53resolver:ListTagsForResource" ]
    },
    "list" : {
      "permissions" : [ "route53resolver:ListFirewallRuleGroupAssociations", "route53resolver:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "route53resolver:DisassociateFirewallRuleGroup", "route53resolver:GetFirewallRuleGroupAssociation", "route53resolver:UntagResource", "route53resolver:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "route53resolver:UpdateFirewallRuleGroupAssociation", "route53resolver:GetFirewallRuleGroupAssociation", "route53resolver:TagResource", "route53resolver:UntagResource", "route53resolver:ListTagsForResource" ]
    }
  }
}