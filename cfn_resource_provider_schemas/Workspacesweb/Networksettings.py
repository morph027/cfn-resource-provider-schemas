SCHEMA = {
  "typeName" : "AWS::WorkSpacesWeb::NetworkSettings",
  "description" : "Definition of AWS::WorkSpacesWeb::NetworkSettings Resource Type",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "AssociatedPortalArns" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 2048,
        "minLength" : 20,
        "pattern" : "^arn:[\\w+=\\/,.@-]+:[a-zA-Z0-9\\-]+:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\\/[a-fA-F0-9\\-]{36})+$"
      },
      "insertionOrder" : False
    },
    "NetworkSettingsArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[\\w+=\\/,.@-]+:[a-zA-Z0-9\\-]+:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\\/[a-fA-F0-9\\-]{36})+$"
    },
    "SecurityGroupIds" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 128,
        "minLength" : 1,
        "pattern" : "^[\\w+\\-]+$"
      },
      "maxItems" : 5,
      "minItems" : 1,
      "insertionOrder" : False
    },
    "SubnetIds" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 32,
        "minLength" : 1,
        "pattern" : "^subnet-([0-9a-f]{8}|[0-9a-f]{17})$"
      },
      "maxItems" : 3,
      "minItems" : 2,
      "insertionOrder" : False
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 0,
      "insertionOrder" : False
    },
    "VpcId" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^vpc-[0-9a-z]*$"
    }
  },
  "required" : [ "SecurityGroupIds", "SubnetIds", "VpcId" ],
  "readOnlyProperties" : [ "/properties/AssociatedPortalArns", "/properties/NetworkSettingsArn" ],
  "primaryIdentifier" : [ "/properties/NetworkSettingsArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "workspaces-web:CreateNetworkSettings", "workspaces-web:GetNetworkSettings", "workspaces-web:ListTagsForResource", "workspaces-web:TagResource" ]
    },
    "read" : {
      "permissions" : [ "workspaces-web:GetNetworkSettings", "workspaces-web:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "workspaces-web:UpdateNetworkSettings", "workspaces-web:UpdateResource", "workspaces-web:TagResource", "workspaces-web:UntagResource", "workspaces-web:GetNetworkSettings", "workspaces-web:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "workspaces-web:GetNetworkSettings", "workspaces-web:DeleteNetworkSettings" ]
    },
    "list" : {
      "permissions" : [ "workspaces-web:ListNetworkSettings" ]
    }
  },
  "tagging" : {
    "cloudFormationSystemTags" : False,
    "tagOnCreate" : True,
    "tagProperty" : "/properties/Tags",
    "tagUpdatable" : True,
    "taggable" : True,
    "permissions" : [ "workspaces-web:UntagResource", "workspaces-web:ListTagsForResource", "workspaces-web:TagResource" ]
  },
  "additionalProperties" : False
}