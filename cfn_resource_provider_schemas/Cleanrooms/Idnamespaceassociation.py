SCHEMA = {
  "typeName" : "AWS::CleanRooms::IdNamespaceAssociation",
  "description" : "Represents an association between an ID namespace and a collaboration",
  "definitions" : {
    "UUID" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    },
    "Document" : {
      "type" : "object"
    },
    "IdNamespaceAssociationInputReferenceConfig" : {
      "type" : "object",
      "properties" : {
        "InputReferenceArn" : {
          "type" : "string",
          "maxLength" : 256
        },
        "ManageResourcePolicies" : {
          "type" : "boolean"
        }
      },
      "required" : [ "InputReferenceArn", "ManageResourcePolicies" ],
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
    },
    "IdMappingConfig" : {
      "type" : "object",
      "properties" : {
        "AllowUseAsDimensionColumn" : {
          "type" : "boolean"
        }
      },
      "required" : [ "AllowUseAsDimensionColumn" ],
      "additionalProperties" : False
    },
    "IdNamespaceAssociationInputReferenceProperties" : {
      "type" : "object",
      "properties" : {
        "IdNamespaceType" : {
          "type" : "string",
          "enum" : [ "SOURCE", "TARGET" ]
        },
        "IdMappingWorkflowsSupported" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/Document"
          }
        }
      },
      "required" : [ ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "IdNamespaceAssociationIdentifier" : {
      "$ref" : "#/definitions/UUID"
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 256
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
    "InputReferenceConfig" : {
      "$ref" : "#/definitions/IdNamespaceAssociationInputReferenceConfig"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "uniqueItems" : True
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "pattern" : "^(?!\\s*$)[\\u0020-\\uD7FF\\uE000-\\uFFFD\\uD800\\uDBFF-\\uDC00\\uDFFF\\t]*$"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 255,
      "pattern" : "^[\\u0020-\\uD7FF\\uE000-\\uFFFD\\uD800\\uDBFF-\\uDC00\\uDFFF\\t\\r\\n]*$"
    },
    "IdMappingConfig" : {
      "$ref" : "#/definitions/IdMappingConfig"
    },
    "InputReferenceProperties" : {
      "$ref" : "#/definitions/IdNamespaceAssociationInputReferenceProperties"
    }
  },
  "required" : [ "MembershipIdentifier", "InputReferenceConfig", "Name" ],
  "readOnlyProperties" : [ "/properties/IdNamespaceAssociationIdentifier", "/properties/Arn", "/properties/MembershipArn", "/properties/CollaborationIdentifier", "/properties/CollaborationArn", "/properties/InputReferenceProperties" ],
  "createOnlyProperties" : [ "/properties/MembershipIdentifier", "/properties/InputReferenceConfig" ],
  "primaryIdentifier" : [ "/properties/IdNamespaceAssociationIdentifier", "/properties/MembershipIdentifier" ],
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
      "permissions" : [ "cleanrooms:CreateIdNamespaceAssociation", "cleanrooms:GetIdNamespaceAssociation", "cleanrooms:ListIdNamespaceAssociations", "cleanrooms:ListTagsForResource", "cleanrooms:TagResource", "cleanrooms:GetMembership", "cleanrooms:GetCollaboration", "entityresolution:GetIdNamespace", "entityresolution:AddPolicyStatement" ]
    },
    "read" : {
      "permissions" : [ "cleanrooms:GetIdNamespaceAssociation", "cleanrooms:ListTagsForResource", "cleanrooms:GetMembership", "cleanrooms:GetCollaboration", "entityresolution:GetIdNamespace" ]
    },
    "update" : {
      "permissions" : [ "cleanrooms:UpdateIdNamespaceAssociation", "cleanrooms:GetIdNamespaceAssociation", "cleanrooms:GetMembership", "cleanrooms:GetCollaboration", "cleanrooms:ListTagsForResource", "cleanrooms:TagResource", "cleanrooms:UntagResource", "entityresolution:GetIdNamespace", "entityresolution:AddPolicyStatement" ]
    },
    "delete" : {
      "permissions" : [ "cleanrooms:DeleteIdNamespaceAssociation", "cleanrooms:GetIdNamespaceAssociation", "cleanrooms:ListIdNamespaceAssociations", "cleanrooms:GetMembership", "cleanrooms:GetCollaboration", "cleanrooms:ListTagsForResource", "cleanrooms:UntagResource", "entityresolution:GetIdNamespace", "entityresolution:DeletePolicyStatement" ]
    },
    "list" : {
      "permissions" : [ "cleanrooms:ListIdNamespaceAssociations", "cleanrooms:GetMembership", "cleanrooms:GetCollaboration" ],
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