SCHEMA = {
  "typeName" : "AWS::Route53Resolver::FirewallDomainList",
  "description" : "Resource schema for AWS::Route53Resolver::FirewallDomainList.",
  "definitions" : {
    "Domains" : {
      "description" : "An inline list of domains to use for this domain list.",
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "description" : "FirewallDomainName",
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 255
      }
    },
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
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "route53resolver:TagResource", "route53resolver:UntagResource" ]
  },
  "properties" : {
    "Id" : {
      "description" : "ResourceId",
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
    "Name" : {
      "description" : "FirewallDomainListName",
      "type" : "string",
      "pattern" : "(?!^[0-9]+$)([a-zA-Z0-9\\-_' ']+)",
      "minLength" : 1,
      "maxLength" : 64
    },
    "DomainCount" : {
      "description" : "Count",
      "type" : "integer",
      "minimum" : 0
    },
    "Status" : {
      "description" : "ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.",
      "type" : "string",
      "enum" : [ "COMPLETE", "DELETING", "UPDATING", "COMPLETE_IMPORT_FAILED", "IMPORTING", "INACTIVE_OWNER_ACCOUNT_CLOSED" ]
    },
    "StatusMessage" : {
      "description" : "FirewallDomainListAssociationStatus",
      "type" : "string"
    },
    "ManagedOwnerName" : {
      "description" : "ServicePrincipal",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 512
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
    "Domains" : {
      "$ref" : "#/definitions/Domains"
    },
    "DomainFileUrl" : {
      "description" : "S3 URL to import domains from.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1024
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
  "createOnlyProperties" : [ "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn", "/properties/DomainCount", "/properties/Status", "/properties/StatusMessage", "/properties/ManagedOwnerName", "/properties/CreatorRequestId", "/properties/CreationTime", "/properties/ModificationTime" ],
  "writeOnlyProperties" : [ "/properties/Domains", "/properties/DomainFileUrl" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "route53resolver:CreateFirewallDomainList", "route53resolver:GetFirewallDomainList", "route53resolver:ImportFirewallDomains", "route53resolver:UpdateFirewallDomains", "route53resolver:TagResource", "route53resolver:ListTagsForResource" ]
    },
    "list" : {
      "permissions" : [ "route53resolver:ListFirewallDomainLists", "route53resolver:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "route53resolver:GetFirewallDomainList", "route53resolver:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "route53resolver:GetFirewallDomainList", "route53resolver:DeleteFirewallDomainList", "route53resolver:UntagResource", "route53resolver:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "route53resolver:GetFirewallDomainList", "route53resolver:ImportFirewallDomains", "route53resolver:UpdateFirewallDomains", "route53resolver:TagResource", "route53resolver:UntagResource", "route53resolver:ListTagsForResource" ]
    }
  }
}