SCHEMA = {
  "typeName" : "AWS::CleanRooms::IdMappingTable",
  "description" : "Represents an association between an ID mapping workflow and a collaboration",
  "definitions" : {
    "UUID" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    },
    "IdMappingTableInputReferenceConfig" : {
      "type" : "object",
      "properties" : {
        "InputReferenceArn" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 20
        },
        "ManageResourcePolicies" : {
          "type" : "boolean"
        }
      },
      "required" : [ "InputReferenceArn", "ManageResourcePolicies" ],
      "additionalProperties" : False
    },
    "IdMappingTableInputSource" : {
      "type" : "object",
      "properties" : {
        "IdNamespaceAssociationId" : {
          "type" : "string"
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "SOURCE", "TARGET" ]
        }
      },
      "required" : [ "IdNamespaceAssociationId", "Type" ],
      "additionalProperties" : False
    },
    "IdMappingTableInputReferenceProperties" : {
      "type" : "object",
      "properties" : {
        "IdMappingTableInputSource" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/IdMappingTableInputSource"
          },
          "maxItems" : 2,
          "minItems" : 2
        }
      },
      "required" : [ "IdMappingTableInputSource" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "IdMappingTableIdentifier" : {
      "$ref" : "#/definitions/UUID"
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 200
    },
    "InputReferenceConfig" : {
      "$ref" : "#/definitions/IdMappingTableInputReferenceConfig"
    },
    "MembershipIdentifier" : {
      "$ref" : "#/definitions/UUID"
    },
    "MembershipArn" : {
      "type" : "string",
      "maxLength" : 100
    },
    "CollaborationIdentifier" : {
      "$ref" : "#/definitions/UUID"
    },
    "CollaborationArn" : {
      "type" : "string",
      "maxLength" : 100
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 255,
      "pattern" : "^[\\u0020-\\uD7FF\\uE000-\\uFFFD\\uD800\\uDBFF-\\uDC00\\uDFFF\\t\\r\\n]*$"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 128,
      "pattern" : "^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$"
    },
    "InputReferenceProperties" : {
      "$ref" : "#/definitions/IdMappingTableInputReferenceProperties"
    },
    "KmsKeyArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 4
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "uniqueItems" : True
    }
  },
  "required" : [ "MembershipIdentifier", "Name", "InputReferenceConfig" ],
  "readOnlyProperties" : [ "/properties/IdMappingTableIdentifier", "/properties/Arn", "/properties/MembershipArn", "/properties/CollaborationIdentifier", "/properties/CollaborationArn", "/properties/InputReferenceProperties" ],
  "createOnlyProperties" : [ "/properties/MembershipIdentifier", "/properties/Name", "/properties/InputReferenceConfig" ],
  "primaryIdentifier" : [ "/properties/IdMappingTableIdentifier", "/properties/MembershipIdentifier" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "cleanrooms:ListTagsForResource", "cleanrooms:UntagResource", "cleanrooms:TagResource" ]
  },
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cleanrooms",
  "handlers" : {
    "create" : {
      "permissions" : [ "cleanrooms:CreateIdMappingTable", "cleanrooms:GetIdMappingTable", "cleanrooms:ListIdMappingTables", "cleanrooms:ListTagsForResource", "cleanrooms:TagResource", "cleanrooms:GetMembership", "cleanrooms:GetCollaboration", "entityresolution:GetIdMappingWorkflow", "entityresolution:AddPolicyStatement" ]
    },
    "read" : {
      "permissions" : [ "cleanrooms:GetIdMappingTable", "cleanrooms:ListTagsForResource", "cleanrooms:GetMembership", "cleanrooms:GetCollaboration" ]
    },
    "update" : {
      "permissions" : [ "cleanrooms:UpdateIdMappingTable", "cleanrooms:GetIdMappingTable", "cleanrooms:GetMembership", "cleanrooms:ListTagsForResource", "cleanrooms:TagResource", "cleanrooms:UntagResource", "entityresolution:GetIdMappingWorkflow", "entityresolution:AddPolicyStatement" ]
    },
    "delete" : {
      "permissions" : [ "cleanrooms:DeleteIdMappingTable", "cleanrooms:GetIdMappingTable", "cleanrooms:ListIdMappingTables", "cleanrooms:GetMembership", "cleanrooms:ListTagsForResource", "cleanrooms:UntagResource", "entityresolution:GetIdMappingWorkflow", "entityresolution:AddPolicyStatement", "entityresolution:DeletePolicyStatement" ]
    },
    "list" : {
      "permissions" : [ "cleanrooms:ListIdMappingTables", "cleanrooms:GetMembership", "cleanrooms:GetCollaboration" ],
      "handlerSchema" : {
        "properties" : {
          "MembershipIdentifier" : {
            "$ref" : "resource-schema.json#/properties/MembershipIdentifier"
          }
        },
        "required" : [ "MembershipIdentifier" ]
      }
    }
  },
  "additionalProperties" : False
}