SCHEMA = {
  "typeName" : "AWS::WAFv2::RegexPatternSet",
  "description" : "Contains a list of Regular expressions based on the provided inputs. RegexPatternSet can be used with other WAF entities with RegexPatternSetReferenceStatement to perform other actions .",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-wafv2.git",
  "definitions" : {
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
      "description" : "ARN of the WAF entity.",
      "type" : "string"
    },
    "Description" : {
      "description" : "Description of the entity.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9=:#@/\\-,.][a-zA-Z0-9+=:#@/\\-,.\\s]+[a-zA-Z0-9+=:#@/\\-,.]{1,256}$"
    },
    "Name" : {
      "description" : "Name of the RegexPatternSet.",
      "type" : "string",
      "pattern" : "^[0-9A-Za-z_-]{1,128}$"
    },
    "Id" : {
      "description" : "Id of the RegexPatternSet",
      "type" : "string",
      "pattern" : "^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$"
    },
    "RegularExpressionList" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "Scope" : {
      "description" : "Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.",
      "type" : "string",
      "enum" : [ "CLOUDFRONT", "REGIONAL" ]
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 1
    }
  },
  "required" : [ "Scope", "RegularExpressionList" ],
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
      "permissions" : [ "wafv2:CreateRegexPatternSet", "wafv2:GetRegexPatternSet", "wafv2:TagResource", "wafv2:UntagResource", "wafv2:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "wafv2:DeleteRegexPatternSet", "wafv2:GetRegexPatternSet" ]
    },
    "read" : {
      "permissions" : [ "wafv2:GetRegexPatternSet", "wafv2:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "wafv2:UpdateRegexPatternSet", "wafv2:GetRegexPatternSet", "wafv2:ListTagsForResource", "wafv2:TagResource", "wafv2:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "wafv2:listRegexPatternSets" ],
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