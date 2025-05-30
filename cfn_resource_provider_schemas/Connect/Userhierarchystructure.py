SCHEMA = {
  "typeName" : "AWS::Connect::UserHierarchyStructure",
  "description" : "Resource Type definition for AWS::Connect::UserHierarchyStructure",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : {
    "Name" : {
      "description" : "The name of the hierarchy level.",
      "type" : "string"
    },
    "HierarchyLevelArn" : {
      "description" : "The Amazon Resource Name (ARN) of the hierarchy level.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/agent-group-level/[-0-9]*$"
    },
    "HierarchyLevelId" : {
      "description" : "The identifier of the hierarchy level.",
      "type" : "string"
    },
    "LevelOne" : {
      "description" : "Information about level one.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HierarchyLevelArn" : {
          "$ref" : "#/definitions/HierarchyLevelArn"
        },
        "HierarchyLevelId" : {
          "$ref" : "#/definitions/HierarchyLevelId"
        },
        "Name" : {
          "$ref" : "#/definitions/Name"
        }
      },
      "required" : [ "Name" ]
    },
    "LevelTwo" : {
      "description" : "Information about level two.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HierarchyLevelArn" : {
          "$ref" : "#/definitions/HierarchyLevelArn"
        },
        "HierarchyLevelId" : {
          "$ref" : "#/definitions/HierarchyLevelId"
        },
        "Name" : {
          "$ref" : "#/definitions/Name"
        }
      },
      "required" : [ "Name" ]
    },
    "LevelThree" : {
      "description" : "Information about level three.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HierarchyLevelArn" : {
          "$ref" : "#/definitions/HierarchyLevelArn"
        },
        "HierarchyLevelId" : {
          "$ref" : "#/definitions/HierarchyLevelId"
        },
        "Name" : {
          "$ref" : "#/definitions/Name"
        }
      },
      "required" : [ "Name" ]
    },
    "LevelFour" : {
      "description" : "Information about level four.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HierarchyLevelArn" : {
          "$ref" : "#/definitions/HierarchyLevelArn"
        },
        "HierarchyLevelId" : {
          "$ref" : "#/definitions/HierarchyLevelId"
        },
        "Name" : {
          "$ref" : "#/definitions/Name"
        }
      },
      "required" : [ "Name" ]
    },
    "LevelFive" : {
      "description" : "Information about level five.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HierarchyLevelArn" : {
          "$ref" : "#/definitions/HierarchyLevelArn"
        },
        "HierarchyLevelId" : {
          "$ref" : "#/definitions/HierarchyLevelId"
        },
        "Name" : {
          "$ref" : "#/definitions/Name"
        }
      },
      "required" : [ "Name" ]
    }
  },
  "properties" : {
    "InstanceArn" : {
      "description" : "The identifier of the Amazon Connect instance.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$"
    },
    "UserHierarchyStructureArn" : {
      "description" : "The identifier of the User Hierarchy Structure.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/user-hierarchy-structure"
    },
    "UserHierarchyStructure" : {
      "description" : "Information about the hierarchy structure.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LevelOne" : {
          "$ref" : "#/definitions/LevelOne"
        },
        "LevelTwo" : {
          "$ref" : "#/definitions/LevelTwo"
        },
        "LevelThree" : {
          "$ref" : "#/definitions/LevelThree"
        },
        "LevelFour" : {
          "$ref" : "#/definitions/LevelFour"
        },
        "LevelFive" : {
          "$ref" : "#/definitions/LevelFive"
        }
      }
    }
  },
  "required" : [ "InstanceArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:UpdateUserHierarchyStructure" ]
    },
    "read" : {
      "permissions" : [ "connect:DescribeUserHierarchyStructure" ]
    },
    "delete" : {
      "permissions" : [ "connect:UpdateUserHierarchyStructure" ]
    },
    "update" : {
      "permissions" : [ "connect:UpdateUserHierarchyStructure" ]
    }
  },
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/InstanceArn" ],
  "primaryIdentifier" : [ "/properties/UserHierarchyStructureArn" ],
  "readOnlyProperties" : [ "/properties/UserHierarchyStructureArn" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  }
}