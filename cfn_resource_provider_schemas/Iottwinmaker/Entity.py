SCHEMA = {
  "typeName" : "AWS::IoTTwinMaker::Entity",
  "description" : "Resource schema for AWS::IoTTwinMaker::Entity",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iottwinmaker",
  "definitions" : {
    "DateTimeFormat" : {
      "type" : "string",
      "format" : "date-time"
    },
    "Relationship" : {
      "description" : "The type of the relationship.",
      "type" : "object",
      "properties" : {
        "RelationshipType" : {
          "description" : "The type of the relationship.",
          "type" : "string",
          "pattern" : ".*",
          "minLength" : 1,
          "maxLength" : 256
        },
        "TargetComponentTypeId" : {
          "description" : "The ID of the target component type associated with this relationship.",
          "type" : "string",
          "pattern" : "[a-zA-Z_\\.\\-0-9:]+",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False
    },
    "PropertyDefinitionConfiguration" : {
      "description" : "An object that specifies information about a property configuration.",
      "type" : "object",
      "patternProperties" : {
        "[a-zA-Z_\\-0-9]+" : {
          "type" : "string",
          "pattern" : "[a-zA-Z_\\-0-9]+",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False
    },
    "DataType" : {
      "description" : "An object that specifies the data type of a property.",
      "type" : "object",
      "properties" : {
        "AllowedValues" : {
          "description" : "The allowed values for this data type.",
          "type" : "array",
          "minItems" : 0,
          "maxItems" : 50,
          "uniqueItems" : False,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/DataValue"
          }
        },
        "NestedType" : {
          "description" : "The nested type in the data type.",
          "$ref" : "#/definitions/DataType"
        },
        "Relationship" : {
          "description" : "A relationship that associates a component with another component.",
          "$ref" : "#/definitions/Relationship"
        },
        "Type" : {
          "description" : "The underlying type of the data type.",
          "type" : "string",
          "enum" : [ "RELATIONSHIP", "STRING", "LONG", "BOOLEAN", "INTEGER", "DOUBLE", "LIST", "MAP" ]
        },
        "UnitOfMeasure" : {
          "description" : "The unit of measure used in this data type.",
          "type" : "string",
          "pattern" : ".*",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False
    },
    "DataValue" : {
      "description" : "An object that specifies a value for a property.",
      "type" : "object",
      "properties" : {
        "BooleanValue" : {
          "description" : "A Boolean value.",
          "type" : "boolean"
        },
        "DoubleValue" : {
          "description" : "A double value.",
          "type" : "number"
        },
        "Expression" : {
          "description" : "An expression that produces the value.",
          "type" : "string",
          "pattern" : "(^\\$\\{Parameters\\.[a-zA-z]+([a-zA-z_0-9]*)}$)",
          "minLength" : 1,
          "maxLength" : 316
        },
        "IntegerValue" : {
          "description" : "An integer value.",
          "type" : "integer"
        },
        "ListValue" : {
          "description" : "A list of multiple values.",
          "type" : "array",
          "minItems" : 0,
          "maxItems" : 50,
          "uniqueItems" : False,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/DataValue"
          }
        },
        "LongValue" : {
          "description" : "A long value.",
          "type" : "number"
        },
        "StringValue" : {
          "description" : "A string value.",
          "type" : "string",
          "pattern" : ".*",
          "minLength" : 1,
          "maxLength" : 256
        },
        "MapValue" : {
          "description" : "An object that maps strings to multiple DataValue objects.",
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z_\\-0-9]+" : {
              "$ref" : "#/definitions/DataValue"
            }
          },
          "additionalProperties" : False
        },
        "RelationshipValue" : {
          "description" : "A value that relates a component to another component.",
          "type" : "object",
          "properties" : {
            "TargetComponentName" : {
              "type" : "string",
              "pattern" : "[a-zA-Z_\\-0-9]+",
              "minLength" : 1,
              "maxLength" : 256
            },
            "TargetEntityId" : {
              "type" : "string",
              "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\\-0-9.:]*[a-zA-Z0-9]+",
              "minLength" : 1,
              "maxLength" : 128
            }
          },
          "additionalProperties" : False
        }
      },
      "additionalProperties" : False
    },
    "Definition" : {
      "description" : "An object that specifies information about a property definition.",
      "type" : "object",
      "properties" : {
        "Configuration" : {
          "description" : "An object that specifies information about a property configuration.",
          "$ref" : "#/definitions/PropertyDefinitionConfiguration"
        },
        "DataType" : {
          "description" : "An object that contains information about the data type.",
          "$ref" : "#/definitions/DataType"
        },
        "DefaultValue" : {
          "description" : "An object that contains the default value.",
          "$ref" : "#/definitions/DataValue"
        },
        "IsExternalId" : {
          "description" : "A Boolean value that specifies whether the property ID comes from an external data store.",
          "type" : "boolean"
        },
        "IsFinal" : {
          "description" : "A Boolean value that specifies whether the property definition can be updated.",
          "type" : "boolean"
        },
        "IsImported" : {
          "description" : "A Boolean value that specifies whether the property definition is imported from an external data store.",
          "type" : "boolean"
        },
        "IsInherited" : {
          "description" : "A Boolean value that specifies whether the property definition is inherited from a parent entity.",
          "type" : "boolean"
        },
        "IsRequiredInEntity" : {
          "description" : "A Boolean value that specifies whether the property is required.",
          "type" : "boolean"
        },
        "IsStoredExternally" : {
          "description" : "A Boolean value that specifies whether the property is stored externally.",
          "type" : "boolean"
        },
        "IsTimeSeries" : {
          "description" : "A Boolean value that specifies whether the property consists of time series data.",
          "type" : "boolean"
        }
      },
      "additionalProperties" : False
    },
    "Property" : {
      "description" : "An object that specifies information about a property.",
      "type" : "object",
      "properties" : {
        "Definition" : {
          "description" : "The definition of the property.",
          "$ref" : "#/definitions/Definition"
        },
        "Value" : {
          "description" : "The value of the property.",
          "$ref" : "#/definitions/DataValue"
        }
      },
      "additionalProperties" : False
    },
    "PropertyName" : {
      "type" : "string",
      "pattern" : "[a-zA-Z_\\-0-9]+"
    },
    "PropertyGroup" : {
      "description" : "An object that specifies information about a property group.",
      "type" : "object",
      "properties" : {
        "GroupType" : {
          "description" : "The type of property group.",
          "type" : "string",
          "enum" : [ "TABULAR" ]
        },
        "PropertyNames" : {
          "description" : "The list of property names in the property group.",
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 256,
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/PropertyName"
          }
        }
      },
      "additionalProperties" : False
    },
    "Component" : {
      "type" : "object",
      "properties" : {
        "ComponentName" : {
          "description" : "The name of the component.",
          "type" : "string",
          "pattern" : "[a-zA-Z_\\-0-9]+",
          "minLength" : 1,
          "maxLength" : 256
        },
        "ComponentTypeId" : {
          "description" : "The ID of the component type.",
          "type" : "string",
          "pattern" : "[a-zA-Z_\\-0-9]+",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Description" : {
          "description" : "The description of the component.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 512
        },
        "DefinedIn" : {
          "description" : "The name of the property definition set in the component.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Properties" : {
          "description" : "An object that maps strings to the properties to set in the component type. Each string in the mapping must be unique to this object.",
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z_\\-0-9]+" : {
              "$ref" : "#/definitions/Property"
            }
          },
          "additionalProperties" : False
        },
        "PropertyGroups" : {
          "description" : "An object that maps strings to the property groups to set in the component type. Each string in the mapping must be unique to this object.",
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z_\\-0-9]+" : {
              "$ref" : "#/definitions/PropertyGroup"
            }
          },
          "additionalProperties" : False
        },
        "Status" : {
          "description" : "The current status of the entity.",
          "$ref" : "#/definitions/Status"
        }
      },
      "additionalProperties" : False
    },
    "CompositeComponent" : {
      "type" : "object",
      "properties" : {
        "ComponentName" : {
          "description" : "The name of the component.",
          "type" : "string",
          "pattern" : "[a-zA-Z_\\-0-9]+",
          "minLength" : 1,
          "maxLength" : 256
        },
        "ComponentPath" : {
          "description" : "The path of the component.",
          "type" : "string",
          "pattern" : "[a-zA-Z_\\-0-9/]+",
          "minLength" : 1,
          "maxLength" : 256
        },
        "ComponentTypeId" : {
          "description" : "The ID of the component type.",
          "type" : "string",
          "pattern" : "[a-zA-Z_\\-0-9]+",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Description" : {
          "description" : "The description of the component.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 512
        },
        "Properties" : {
          "description" : "An object that maps strings to the properties to set in the component type. Each string in the mapping must be unique to this object.",
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z_\\-0-9]+" : {
              "$ref" : "#/definitions/Property"
            }
          },
          "additionalProperties" : False
        },
        "PropertyGroups" : {
          "description" : "An object that maps strings to the property groups to set in the component type. Each string in the mapping must be unique to this object.",
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z_\\-0-9]+" : {
              "$ref" : "#/definitions/PropertyGroup"
            }
          },
          "additionalProperties" : False
        },
        "Status" : {
          "description" : "The current status of the component.",
          "$ref" : "#/definitions/Status"
        }
      },
      "additionalProperties" : False
    },
    "Status" : {
      "type" : "object",
      "properties" : {
        "State" : {
          "type" : "string",
          "enum" : [ "CREATING", "UPDATING", "DELETING", "ACTIVE", "ERROR" ]
        },
        "Error" : {
          "type" : "object",
          "anyOf" : [ {
            "description" : "Empty Error object.",
            "type" : "object",
            "additionalProperties" : False
          }, {
            "description" : "Error object with Message and Code.",
            "type" : "object",
            "properties" : {
              "Message" : {
                "type" : "string",
                "minLength" : 0,
                "maxLength" : 2048
              },
              "Code" : {
                "type" : "string",
                "enum" : [ "VALIDATION_ERROR", "INTERNAL_FAILURE" ]
              }
            },
            "additionalProperties" : False
          } ]
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "EntityId" : {
      "description" : "The ID of the entity.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\\-0-9.:]*[a-zA-Z0-9]+"
    },
    "EntityName" : {
      "description" : "The name of the entity.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "[a-zA-Z_0-9-.][a-zA-Z_0-9-. ]*[a-zA-Z0-9]+"
    },
    "Status" : {
      "description" : "The current status of the entity.",
      "$ref" : "#/definitions/Status"
    },
    "HasChildEntities" : {
      "description" : "A Boolean value that specifies whether the entity has child entities or not.",
      "type" : "boolean"
    },
    "ParentEntityId" : {
      "description" : "The ID of the parent entity.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "\\$ROOT|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\\-0-9.:]*[a-zA-Z0-9]+"
    },
    "Arn" : {
      "description" : "The ARN of the entity.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048,
      "pattern" : "arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\\/a-zA-Z0-9_\\-\\.:]+"
    },
    "Description" : {
      "description" : "The description of the entity.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 512
    },
    "CreationDateTime" : {
      "description" : "The date and time when the entity was created.",
      "$ref" : "#/definitions/DateTimeFormat"
    },
    "UpdateDateTime" : {
      "description" : "The last date and time when the entity was updated.",
      "$ref" : "#/definitions/DateTimeFormat"
    },
    "Tags" : {
      "type" : "object",
      "description" : "A key-value pair to associate with a resource.",
      "patternProperties" : {
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False
    },
    "WorkspaceId" : {
      "description" : "The ID of the workspace.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "[a-zA-Z_0-9][a-zA-Z_\\-0-9]*[a-zA-Z0-9]+"
    },
    "Components" : {
      "description" : "A map that sets information about a component type.",
      "type" : "object",
      "patternProperties" : {
        "[a-zA-Z_\\-0-9]+" : {
          "$ref" : "#/definitions/Component"
        }
      },
      "additionalProperties" : False
    },
    "CompositeComponents" : {
      "description" : "A map that sets information about a composite component.",
      "type" : "object",
      "patternProperties" : {
        "[a-zA-Z_\\-0-9/]+" : {
          "$ref" : "#/definitions/CompositeComponent"
        }
      },
      "additionalProperties" : False
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iottwinmaker:TagResource", "iottwinmaker:UntagResource", "iottwinmaker:ListTagsForResource" ]
  },
  "required" : [ "WorkspaceId", "EntityName" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreationDateTime", "/properties/UpdateDateTime", "/properties/Status", "/properties/HasChildEntities" ],
  "createOnlyProperties" : [ "/properties/WorkspaceId", "/properties/EntityId" ],
  "primaryIdentifier" : [ "/properties/WorkspaceId", "/properties/EntityId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iottwinmaker:GetWorkspace", "iottwinmaker:CreateEntity", "iottwinmaker:GetEntity", "iottwinmaker:ListComponents", "iottwinmaker:ListProperties", "iottwinmaker:ListTagsForResource", "iottwinmaker:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iottwinmaker:GetComponentType", "iottwinmaker:GetEntity", "iottwinmaker:ListComponents", "iottwinmaker:ListProperties", "iottwinmaker:GetWorkspace", "iottwinmaker:ListEntities", "iottwinmaker:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iottwinmaker:GetComponentType", "iottwinmaker:GetEntity", "iottwinmaker:ListComponents", "iottwinmaker:ListProperties", "iottwinmaker:GetWorkspace", "iottwinmaker:ListTagsForResource", "iottwinmaker:TagResource", "iottwinmaker:UntagResource", "iottwinmaker:UpdateEntity", "iottwinmaker:UpdateComponentType" ]
    },
    "delete" : {
      "permissions" : [ "iottwinmaker:GetEntity", "iottwinmaker:GetWorkspace", "iottwinmaker:DeleteEntity" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "WorkspaceId" : {
            "type" : "string",
            "$ref" : "resource-schema.json#/properties/WorkspaceId"
          }
        },
        "required" : [ "WorkspaceId" ]
      },
      "permissions" : [ "iottwinmaker:GetWorkspace", "iottwinmaker:ListTagsForResource", "iottwinmaker:GetEntity", "iottwinmaker:ListEntities" ]
    }
  }
}