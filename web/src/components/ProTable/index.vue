<!--
 *                        .::::.
 *                      .::::::::.
 *                     :::::::::::
 *                  ..:::::::::::'
 *               '::::::::::::'
 *                 .::::::::::
 *            '::::::::::::::..
 *                 ..::::::::::::.
 *               ``::::::::::::::::
 *                ::::``:::::::::'        .:::.
 *               ::::'   ':::::'       .::::::::.
 *             .::::'      ::::     .:::::::'::::.
 *            .:::'       :::::  .:::::::::' ':::::.
 *           .::'        :::::.:::::::::'      ':::::.
 *          .::'         ::::::::::::::'         ``::::.
 *      ...:::           ::::::::::::'              ``::.
 *     ````':.          ':::::::::'                  ::::..
 *                        '.:::::'                    ':'````..
 * 
 * @Description:
 * @version: 
 * @Date: 2021-04-20 11:06:21
 * @LastEditors: cenjinhe@126.com
 * @LastEditTime: 2022-09-25 11:53:47
 * @Author: cenjinhe@126.com
 * @HomePage: https://cenjinhe.gitee.io/Stock-System
 * @Github: https://github.com/cenjinhe/Stock-System
 * @Donate: https://cenjinhe.gitee.io/Stock-System/donate/
 -->

<template>
  <div class="page-box">
    <!-- 搜索选项 -->

    <el-form
      v-if="!!search"
      class="search"
      :model="searchModel"
      :inline="true"
      label-position="right"
      :label-width="search.labelWidth"
      ref="searchForm"
    >
      <el-form-item
        v-for="item in search.fields"
        :key="item.name"
        :label="$t(item.label)"
        :prop="item.name"
      >
        <slot v-if="item.type === 'custom'" :name="item.slot" />
        <el-select
          v-else-if="item.type === 'select'"
          v-model="searchModel[item.name]"
          :filterable="!!item.filterable"
          :multiple="!!item.multiple"
          clearable
          :placeholder="$t(item.label)"
          :style="{ width: search.inputWidth, ...item.style }"
        >
          <el-option
            v-for="option of item.options"
            :key="option.value"
            :label="$t(option.name)"
            :value="option.value"
          ></el-option>
        </el-select>
        <el-radio-group
          v-model="searchModel[item.name]"
          v-else-if="item.type === 'radio'"
          :style="{ width: search.inputWidth, ...item.style }"
        >
          <el-radio
            v-for="option of item.options"
            :key="option.value"
            :label="option.value"
          >
            {{ $t(option.name) }}
          </el-radio>
        </el-radio-group>
        <el-radio-group
          v-model="searchModel[item.name]"
          v-else-if="item.type === 'radio-button'"
          :style="{ width: search.inputWidth, ...item.style }"
        >
          <el-radio-button
            v-for="option of item.options"
            :key="option.value"
            :label="option.value"
          >
            {{ $t(option.name) }}
          </el-radio-button>
        </el-radio-group>
        <el-checkbox-group
          v-model="searchModel[item.name]"
          v-else-if="item.type === 'checkbox'"
          :style="{ width: search.inputWidth, ...item.style }"
        >
          <el-checkbox
            v-for="option of item.options"
            :key="option.value"
            :label="option.value"
          >
            {{ $t(option.name) }}
          </el-checkbox>
        </el-checkbox-group>
        <el-checkbox-group
          v-model="searchModel[item.name]"
          v-else-if="item.type === 'checkbox-button'"
          :style="{ width: search.inputWidth, ...item.style }"
        >
          <el-checkbox-button
            v-for="option of item.options"
            :key="option.value"
            :label="option.value"
          >
            {{ $t(option.name) }}
          </el-checkbox-button>
        </el-checkbox-group>
        <el-date-picker
          v-else-if="item.type === 'date'"
          v-model="searchModel[item.name]"
          type="date"
          format="YYYY-MM-DD"
          clearable
          @change="handleDateChange($event, item, 'YYYY-MM-DD')"
          :placeholder="$t(item.label)"
          :style="{ width: search.inputWidth, ...item.style }"
        ></el-date-picker>
        <el-date-picker
          v-else-if="item.type === 'datetime'"
          v-model="searchModel[item.name]"
          type="datetime"
          clearable
          @change="handleDateChange($event, item, 'YYYY-MM-DD HH:mm:ss')"
          format="YYYY-MM-DD HH:mm:ss"
          :placeholder="$t(item.label)"
          :style="{ width: search.inputWidth, ...item.style }"
        ></el-date-picker>
        <el-date-picker
          v-else-if="item.type === 'daterange'"
          v-model="searchModel[item.name]"
          type="daterange"
          format="YYYY-MM-DD"
          range-separator="-"
          :start-placeholder="$t('public.startdate')"
          :end-placeholder="$t('public.enddate')"
          clearable
          @change="handleRangeChange($event, item, 'YYYY-MM-DD')"
          :style="{ ...item.style }"
        ></el-date-picker>
        <el-date-picker
          v-else-if="item.type === 'datetimerange'"
          v-model="searchModel[item.name]"
          type="datetimerange"
          format="YYYY-MM-DD HH:mm:ss"
          range-separator="-"
          :start-placeholder="$t('public.starttime')"
          :end-placeholder="$t('public.endtime')"
          clearable
          @change="handleRangeChange($event, item, 'YYYY-MM-DD HH:mm:ss')"
          :style="{ ...item.style }"
        ></el-date-picker>
        <el-input-number
          v-else-if="item.type === 'number'"
          v-model="searchModel[item.name]"
          :placeholder="$t(item.label)"
          controls-position="right"
          :min="item.min"
          :max="item.max"
          :style="{ width: search.inputWidth, ...item.style }"
        />
        <el-input
          v-else-if="item.type === 'textarea'"
          :maxlength="item.maxlength"
          type="textarea"
          clearable
          v-model="searchModel[item.name]"
          :placeholder="$t(item.label)"
          :style="{ width: search.inputWidth, ...item.style }"
        ></el-input>
        <el-input
          v-else
          :maxlength="item.maxlength"
          v-model="searchModel[item.name]"
          clearable
          :placeholder="$t(item.label)"
          :style="{ width: search.inputWidth, ...item.style }"
        ></el-input>
      </el-form-item>
      <el-form-item class="search-btn">
        <el-button type="primary" icon="Search" @click="handleSearch">
          {{ $t('public.search') }}
        </el-button>
        <el-button @click="handleReset" icon="RefreshRight">
          {{ $t('public.reset') }}
        </el-button>
      </el-form-item>
    </el-form>

    <!-- title 和 工具栏 -->
    <div class="head" v-if="!hideTitleBar">
      <slot name="title">
        <span class="title">{{ title }}</span>
      </slot>
      <div class="toolbar">
        <slot name="toolbar"></slot>
      </div>
    </div>
    <!-- table表格栏 -->
    <div class="table">
      <el-table
        v-loading="loading"
        :data="tableData"
        :row-key="rowKey"
        tooltip-effect="dark"
        stripe
        :border="border"
        :max-height="maxHeight"
        @selection-change="handleSelectionChange"
        @sort-change="changeTableSort"
      >
        <template v-for="item in columns" :key="item.label">
          <el-table-column
            :filter-method="item.filters && filterHandler"
            :show-overflow-tooltip="!item.wrap"
            v-bind="item"
            :label="item.label ? $t(item.label) : ''"
            v-if="item.isShow || item.isShow === undefined"
          >
            <template #header="scope" v-if="!!item.labelSlot">
              <slot :name="item.labelSlot" v-bind="scope"></slot>
            </template>
            <template #default="scope" v-if="!!item.tdSlot">
              <slot :name="item.tdSlot" v-bind="scope"></slot>
            </template>
        </el-table-column>
        </template>
      </el-table>
    </div>
    <!-- 分页 -->
    <el-pagination
      v-if="paginationConfig.show && total > 0"
      class="pagination"
      :style="paginationConfig.style"
      @size-change="handleSizeChange"
      v-model:currentPage="pageNum"
      @current-change="handleCurrentChange"
      :page-sizes="paginationConfig.pageSizes"
      v-model:pageSize="pageSize"
      :layout="paginationConfig.layout"
      :total="total"
    ></el-pagination>
  </div>
</template>
<script>
import { defineComponent, reactive, toRefs, onBeforeMount, watch } from 'vue'
const formatDate = (date, format) => {
  var obj = {
    'M+': date.getMonth() + 1,
    'D+': date.getDate(),
    'H+': date.getHours(),
    'm+': date.getMinutes(),
    's+': date.getSeconds(),
    'q+': Math.floor((date.getMonth() + 3) / 3),
    'S+': date.getMilliseconds(),
  }
  if (/(y+)/i.test(format)) {
    format = format.replace(
      RegExp.$1,
      (date.getFullYear() + '').substr(4 - RegExp.$1.length)
    )
  }
  for (var k in obj) {
    if (new RegExp('(' + k + ')').test(format)) {
      format = format.replace(
        RegExp.$1,
        RegExp.$1.length == 1
          ? obj[k]
          : ('00' + obj[k]).substr(('' + obj[k]).length)
      )
    }
  }
  return format
}
const getSearchModel = search => {
  const searchModel = {}
  if (search && search.fields) {
    search.fields.forEach(item => {
      switch (item.type) {
        case 'checkbox':
        case 'checkbox-button':
          searchModel[item.name] = []
          break
        default:
          break
      }
      if (item.defaultValue !== undefined) {
        searchModel[item.name] = item.defaultValue
        // 日期范围和时间范围真实变量默认值
        if (
          (item.type === 'daterange' || item.type === 'datetimerange') &&
          !!item.trueNames &&
          Array.isArray(item.defaultValue)
        ) {
          item.defaultValue.forEach((val, index) => {
            searchModel[item.trueNames[index]] = val
          })
        }
      }
    })
  }
  return searchModel
}
export default defineComponent({
  props: {
    // 请求数据的方法
    request: {
      type: Function,
    },
    // 表格标题
    title: {
      type: String,
      default: '',
    },
    // 是否隐藏标题栏
    hideTitleBar: {
      type: Boolean,
      default: false,
    },
    // 是否隐藏按钮操作
    hideToolbar: {
      type: Boolean,
      default: false,
    },
    // 搜索表单配置，false表示不显示搜索表单
    search: {
      type: [Boolean, Object],
      default: false,
    },
    border: {
      type: Boolean,
      default: false,
    },
    maxHeight: {
      type: [Number, String],
      default: 'auto',
    },
    // 表头配置
    columns: {
      type: Array,
      default: () => [],
    },
    // 行数据的Key，同elementUI的table组件的row-key
    rowKey: {
      type: [String, Function],
      default: () => {},
    },
    // 分页配置，false表示不显示分页
    pagination: {
      type: [Boolean, Object],
      default: () => ({}),
    },
  },
  setup(props, { emit }) {
    // 优化搜索字段，
    // 1、如果搜索配置有transform处理函数，执行transform
    // 2、删除日期范围默认的name字段
    const optimizeFields = search => {
      const searchModel = JSON.parse(JSON.stringify(state.searchModel))
      if (search && search.fields) {
        search.fields.forEach(item => {
          if (!searchModel.hasOwnProperty(item.name)) {
            return
          }
          if (item.transform) {
            searchModel[item.name] = item.transform(searchModel[item.name])
          }
          if (
            (item.type === 'daterange' || item.type === 'datetimerange') &&
            !!item.trueNames
          ) {
            delete searchModel[item.name]
          }
        })
      }
      return searchModel
    }

    // 请求列表数据
    const getTableData = async () => {
      state.loading = true
      const searchModel = optimizeFields(props.search)
      const { data, total } = await props.request({
        current: state.pageNum,
        size: state.pageSize,
        ...searchModel,
      })
      state.loading = false
      state.tableData = data
      state.total = total
    }

    const state = reactive({
      searchModel: getSearchModel(props.search),
      loading: false,
      tableData: [],
      total: 0,
      pageNum: 1,
      pageSize: (!!props.pagination && props.pagination.pageSize) || 15,
      paginationConfig: {
        show: false,
      },
      // 搜索
      handleSearch() {
        state.pageNum = 1
        getTableData()
      },
      // 重置函数
      handleReset() {
        if (JSON.stringify(state.searchModel) === '{}') {
          return
        }
        state.pageNum = 1
        state.searchModel = getSearchModel(props.search)
        getTableData()
      },
      // 刷新
      refresh() {
        getTableData()
      },

      // 当前页变化
      handleCurrentChange() {
        getTableData()
      },
      // 改变每页size数量
      handleSizeChange() {
        state.pageNum = 1
        getTableData()
      },
      // 全选
      handleSelectionChange(arr) {
        emit('selectionChange', arr)
      },
      // 排序
      changeTableSort(column) {
        emit('sort-change', column)
      },
      // 过滤方法
      filterHandler(value, row, column) {
        const property = column['property']
        return row[property] === value
      },
      // 日期范围
      handleDateChange(date, item, format) {
        state.searchModel[item.name] = date ? formatDate(date, format) : ''
      },
      handleRangeChange(date, item, format) {
        const arr = !!date && date.map(d => formatDate(d, format))
        state.searchModel[item.name] = arr ? arr : []

        if (!item.trueNames) {
          return
        }

        if (arr) {
          arr.forEach((val, index) => {
            state.searchModel[item.trueNames[index]] = val
          })
        } else {
          item.trueNames.forEach(key => {
            delete state.searchModel[key]
          })
        }
      },
    })

    if (typeof props.pagination === 'object') {
      const { layout, pageSizes, style } = props.pagination
      state.paginationConfig = {
        show: true,
        layout: layout || 'total, sizes, prev, pager, next, jumper',
        pageSizes: pageSizes || [10, 15, 20, 30, 40, 50, 100],
        style: style || {},
      }
    }

    watch(
      () => props.search,
      val => {
        state.searchModel = getSearchModel(val)
      },
      { deep: true }
    )

    onBeforeMount(() => {
      getTableData()
    })

    return {
      ...toRefs(state),
    }
  },
})
</script>
<style lang="scss" scoped>
.page-box {
  width: 100%;
  box-sizing: border-box;
  .search {
    padding: 20px 20px 0;
    background: #fff;
    margin-bottom: 10px;
    display: flex;
    flex-wrap: wrap;
    .el-form-item {
      margin-bottom: 20px;
    }
    .search-btn {
      margin-left: auto;
    }
    :deep(.el-input-number .el-input__inner) {
      text-align: left;
    }
    :deep(.el-range-editor.el-input__wrapper) {
      box-sizing: border-box;
    }
  }

  .head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 20px 0;
    background: #fff;
    .title {
      font-size: 16px;
    }
  }
  .table {
    padding: 20px;
    background: #fff;
  }
  .pagination {
    padding: 0 20px 20px;
    background: #fff;
    justify-content: flex-end;
    :last-child {
      margin-right: 0;
    }
  }
}
</style>
