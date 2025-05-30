SCHEMA = {
  "typeName" : "AWS::CodeArtifact::PackageGroup",
  "description" : "The resource schema to create a CodeArtifact package group.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-codeartifact",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    },
    "OriginConfiguration" : {
      "type" : "object",
      "properties" : {
        "Restrictions" : {
          "description" : "The origin configuration that is applied to the package group.",
          "type" : "object",
          "$ref" : "#/definitions/Restrictions"
        }
      },
      "required" : [ "Restrictions" ],
      "additionalProperties" : False
    },
    "Restrictions" : {
      "type" : "object",
      "properties" : {
        "Publish" : {
          "type" : "object",
          "description" : "The publish restriction determines if new package versions can be published.",
          "$ref" : "#/definitions/RestrictionType"
        },
        "ExternalUpstream" : {
          "type" : "object",
          "description" : "The external upstream restriction determines if new package versions can be ingested or retained from external connections.",
          "$ref" : "#/definitions/RestrictionType"
        },
        "InternalUpstream" : {
          "type" : "object",
          "description" : "The internal upstream restriction determines if new package versions can be ingested or retained from upstream repositories.",
          "$ref" : "#/definitions/RestrictionType"
        }
      },
      "additionalProperties" : False
    },
    "RestrictionType" : {
      "type" : "object",
      "properties" : {
        "RestrictionMode" : {
          "type" : "string",
          "enum" : [ "ALLOW", "BLOCK", "ALLOW_SPECIFIC_REPOSITORIES", "INHERIT" ]
        },
        "Repositories" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        }
      },
      "required" : [ "RestrictionMode" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DomainName" : {
      "description" : "The name of the domain that contains the package group.",
      "type" : "string",
      "pattern" : "^([a-z][a-z0-9\\-]{0,48}[a-z0-9])$",
      "minLength" : 2,
      "maxLength" : 50
    },
    "DomainOwner" : {
      "description" : "The 12-digit account ID of the AWS account that owns the domain.",
      "pattern" : "[0-9]{12}",
      "type" : "string"
    },
    "Pattern" : {
      "description" : "The package group pattern that is used to gather packages.",
      "type" : "string",
      "minLength" : 2,
      "maxLength" : 520
    },
    "ContactInfo" : {
      "description" : "The contact info of the package group.",
      "type" : "string",
      "maxLength" : 1000
    },
    "Description" : {
      "description" : "The text description of the package group.",
      "type" : "string",
      "maxLength" : 1000
    },
    "OriginConfiguration" : {
      "description" : "The package origin configuration of the package group.",
      "type" : "object",
      "$ref" : "#/definitions/OriginConfiguration"
    },
    "Tags" : {
      "type" : "array",
      "description" : "An array of key-value pairs to apply to the package group.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Arn" : {
      "description" : "The ARN of the package group.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    }
  },
  "additionalProperties" : False,
  "required" : [ "Pattern", "DomainName" ],
  "createOnlyProperties" : [ "/properties/DomainName", "/properties/Pattern" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "codeartifact:CreatePackageGroup", "codeartifact:DescribePackageGroup", "codeartifact:UpdatePackageGroup", "codeartifact:UpdatePackageGroupOriginConfiguration", "codeartifact:ListAllowedRepositoriesForGroup", "codeartifact:ListTagsForResource", "codeartifact:TagResource" ]
    },
    "read" : {
      "permissions" : [ "codeartifact:DescribePackageGroup", "codeartifact:ListAllowedRepositoriesForGroup", "codeartifact:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "codeartifact:UpdatePackageGroup", "codeartifact:UpdatePackageGroupOriginConfiguration", "codeartifact:DescribePackageGroup", "codeartifact:ListAllowedRepositoriesForGroup", "codeartifact:ListTagsForResource", "codeartifact:TagResource", "codeartifact:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "codeartifact:DeletePackageGroup", "codeartifact:DescribePackageGroup" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DomainName" : {
            "$ref" : "resource-schema.json#/properties/DomainName"
          }
        },
        "required" : [ "DomainName" ]
      },
      "permissions" : [ "codeartifact:ListPackageGroups" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "codeartifact:ListTagsForResource", "codeartifact:UntagResource", "codeartifact:TagResource" ]
  }
}