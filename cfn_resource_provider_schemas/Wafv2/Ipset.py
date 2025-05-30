SCHEMA = {
  "typeName" : "AWS::WAFv2::IPSet",
  "description" : "Contains a list of IP addresses. This can be either IPV4 or IPV6. The list will be mutually",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-wafv2.git",
  "definitions" : {
    "EntityName" : {
      "description" : "Name of the IPSet.",
      "type" : "string",
      "pattern" : "^[0-9A-Za-z_-]{1,128}$"
    },
    "EntityDescription" : {
      "description" : "Description of the entity.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9=:#@/\\-,.][a-zA-Z0-9+=:#@/\\-,.\\s]+[a-zA-Z0-9+=:#@/\\-,.]{1,256}$"
    },
    "EntityId" : {
      "description" : "Id of the IPSet",
      "type" : "string",
      "pattern" : "^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$"
    },
    "Scope" : {
      "description" : "Use CLOUDFRONT for CloudFront IPSet, use REGIONAL for Application Load Balancer and API Gateway.",
      "type" : "string",
      "enum" : [ "CLOUDFRONT", "REGIONAL" ]
    },
    "IPAddressVersion" : {
      "description" : "Type of addresses in the IPSet, use IPV4 for IPV4 IP addresses, IPV6 for IPV6 address.",
      "type" : "string",
      "enum" : [ "IPV4", "IPV6" ]
    },
    "IPAddress" : {
      "description" : "IP address",
      "type" : "string",
      "maxLength" : 50,
      "minLength" : 1
    },
    "ResourceArn" : {
      "description" : "ARN of the WAF entity.",
      "type" : "string"
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "$ref" : "#/definitions/ResourceArn"
    },
    "Description" : {
      "$ref" : "#/definitions/EntityDescription"
    },
    "Name" : {
      "$ref" : "#/definitions/EntityName"
    },
    "Id" : {
      "$ref" : "#/definitions/EntityId"
    },
    "Scope" : {
      "$ref" : "#/definitions/Scope"
    },
    "IPAddressVersion" : {
      "$ref" : "#/definitions/IPAddressVersion"
    },
    "Addresses" : {
      "description" : "List of IPAddresses.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/IPAddress"
      }
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 1
    }
  },
  "required" : [ "Addresses", "IPAddressVersion", "Scope" ],
  "primaryIdentifier" : [ "/properties/Name", "/properties/Id", "/properties/Scope" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Scope" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id" ],
  "additionalProperties" : False,
  "tagging" : {
    "cloudFormationSystemTags" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "taggable" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "wafv2:TagResource", "wafv2:UntagResource", "wafv2:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "wafv2:CreateIPSet", "wafv2:GetIPSet", "wafv2:ListTagsForResource", "wafv2:TagResource", "wafv2:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "wafv2:DeleteIPSet", "wafv2:GetIPSet" ]
    },
    "read" : {
      "permissions" : [ "wafv2:GetIPSet", "wafv2:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "wafv2:UpdateIPSet", "wafv2:GetIPSet", "wafv2:ListTagsForResource", "wafv2:TagResource", "wafv2:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "wafv2:listIPSets" ],
      "handlerSchema" : {
        "properties" : {
          "Scope" : {
            "$ref" : "resource-schema.json#/properties/Scope"
          }
        },
        "required" : [ "Scope" ]
      }
    }
  }
}