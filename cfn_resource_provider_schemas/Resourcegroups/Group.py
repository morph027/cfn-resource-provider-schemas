SCHEMA = {
  "typeName" : "AWS::ResourceGroups::Group",
  "description" : "Schema for ResourceGroups::Group",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "ResourceQuery" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "type" : "string",
          "enum" : [ "TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0" ]
        },
        "Query" : {
          "$ref" : "#/definitions/Query"
        }
      },
      "additionalProperties" : False
    },
    "Query" : {
      "type" : "object",
      "properties" : {
        "ResourceTypeFilters" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "StackIdentifier" : {
          "type" : "string"
        },
        "TagFilters" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/TagFilter"
          }
        }
      },
      "additionalProperties" : False
    },
    "TagFilter" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Values" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "pattern" : "^(?!aws:).+"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "Configuration" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/ConfigurationItem"
      }
    },
    "ConfigurationItem" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "type" : "string"
        },
        "Parameters" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/ConfigurationParameter"
          }
        }
      },
      "additionalProperties" : False
    },
    "ConfigurationParameter" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string"
        },
        "Values" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name of the resource group",
      "type" : "string",
      "maxLength" : 128
    },
    "Description" : {
      "description" : "The description of the resource group",
      "type" : "string",
      "maxLength" : 512
    },
    "ResourceQuery" : {
      "$ref" : "#/definitions/ResourceQuery"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Arn" : {
      "description" : "The Resource Group ARN.",
      "type" : "string"
    },
    "Configuration" : {
      "$ref" : "#/definitions/Configuration"
    },
    "Resources" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "resource-groups:Tag", "resource-groups:Untag", "resource-groups:GetTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "resource-groups:CreateGroup", "resource-groups:Tag", "cloudformation:DescribeStacks", "cloudformation:ListStackResources", "resource-groups:ListGroupResources", "resource-groups:GroupResources" ]
    },
    "read" : {
      "permissions" : [ "resource-groups:GetGroup", "resource-groups:GetGroupQuery", "resource-groups:GetTags", "resource-groups:GetGroupConfiguration", "resource-groups:ListGroupResources" ]
    },
    "update" : {
      "permissions" : [ "resource-groups:UpdateGroup", "resource-groups:GetTags", "resource-groups:GetGroupQuery", "resource-groups:UpdateGroupQuery", "resource-groups:Tag", "resource-groups:Untag", "resource-groups:PutGroupConfiguration", "resource-groups:GetGroupConfiguration", "resource-groups:ListGroupResources", "resource-groups:GroupResources", "resource-groups:UnGroupResources" ]
    },
    "delete" : {
      "permissions" : [ "resource-groups:DeleteGroup", "resource-groups:UnGroupResources" ]
    },
    "list" : {
      "permissions" : [ "resource-groups:ListGroups" ]
    }
  }
}